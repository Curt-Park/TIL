package main

import (
	"crypto/rand"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"strings"
	"sync"
	"time"
)

const sessionTTL = 15 * time.Minute

// appSecret signs the app's own session tokens. It has nothing to do with the
// provider: delegating the password check did not delegate the session.
var appSecret = []byte("app-secret-not-for-real-use")

// pending is what the app must remember between sending the user to the
// provider and receiving them back. It is keyed by the state parameter.
type pending struct {
	verifier string
	expires  time.Time
}

var (
	appMu    sync.Mutex
	pendings = map[string]pending{}
	counts   = map[string]int{}
)

func appRoutes() *http.ServeMux {
	mux := http.NewServeMux()
	mux.HandleFunc("GET /login", appLogin)
	mux.HandleFunc("GET /callback", appCallback)
	mux.HandleFunc("GET /whoami", appWhoami)
	return mux
}

// appLogin does not ask for anything. It sends the user to the provider and
// waits to be told who came back.
func appLogin(w http.ResponseWriter, r *http.Request) {
	state := rand.Text()
	verifier := rand.Text()

	appMu.Lock()
	pendings[state] = pending{verifier: verifier, expires: time.Now().Add(5 * time.Minute)}
	appMu.Unlock()

	// PKCE: the hash of the verifier goes out now, the verifier itself only at
	// the token endpoint. Whoever steals the code off the redirect cannot
	// redeem it, because the verifier never travelled through the browser.
	q := url.Values{
		"response_type":         {"code"},
		"client_id":             {clientID},
		"redirect_uri":          {redirectURI},
		"scope":                 {"openid"},
		"state":                 {state},
		"code_challenge":        {challenge(verifier)},
		"code_challenge_method": {"S256"},
	}
	http.Redirect(w, r, issuer+"/authorize?"+q.Encode(), http.StatusFound)
}

func appCallback(w http.ResponseWriter, r *http.Request) {
	q := r.URL.Query()

	// state proves this callback belongs to a flow the app itself started.
	// Consuming it here means a code cannot be replayed against a second visit.
	appMu.Lock()
	p, ok := pendings[q.Get("state")]
	delete(pendings, q.Get("state"))
	appMu.Unlock()
	if !ok || time.Now().After(p.expires) {
		http.Error(w, "unknown or expired state", http.StatusBadRequest)
		return
	}

	idToken, err := redeem(q.Get("code"), p.verifier)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadGateway)
		return
	}

	// The id_token is what makes this authentication rather than authorization.
	// An access token says what the bearer may do; this says who the user is.
	c, ok := verifyJWS([]byte(clientSecret), idToken)
	if !ok || c.Iss != issuer || c.Aud != clientID {
		http.Error(w, "invalid id_token", http.StatusBadGateway)
		return
	}

	// The provider vouched for the user. From here the app runs its own session
	// exactly as it did before.
	fmt.Fprintln(w, signJWS(appSecret, claims{Sub: c.Sub, Exp: time.Now().Add(sessionTTL).Unix()}))
}

// redeem trades the code for tokens. This request goes from the app straight to
// the provider, so neither the code nor clientSecret passes through the browser.
func redeem(code, verifier string) (string, error) {
	resp, err := http.PostForm(issuer+"/token", url.Values{
		"grant_type":    {"authorization_code"},
		"code":          {code},
		"redirect_uri":  {redirectURI},
		"client_id":     {clientID},
		"client_secret": {clientSecret},
		"code_verifier": {verifier},
	})
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		body, _ := io.ReadAll(resp.Body)
		return "", fmt.Errorf("token endpoint said %s: %s", resp.Status, body)
	}

	var out struct {
		AccessToken string `json:"access_token"`
		IDToken     string `json:"id_token"`
	}
	if err := json.NewDecoder(resp.Body).Decode(&out); err != nil {
		return "", err
	}
	return out.IDToken, nil
}

func appWhoami(w http.ResponseWriter, r *http.Request) {
	token, ok := strings.CutPrefix(r.Header.Get("Authorization"), "Bearer ")
	if !ok {
		unauthorized(w, `Bearer realm="whoami"`, "missing token")
		return
	}

	c, ok := verifyJWS(appSecret, token)
	if !ok {
		unauthorized(w, `Bearer realm="whoami", error="invalid_token"`, "invalid token")
		return
	}

	appMu.Lock()
	counts[c.Sub]++
	count := counts[c.Sub]
	appMu.Unlock()

	fmt.Fprintf(w, "%s: %d\n", c.Sub, count)
}

// unauthorized rejects a request with a challenge. RFC 9110 requires every 401
// to carry a WWW-Authenticate header telling the client how to authenticate.
func unauthorized(w http.ResponseWriter, challenge, msg string) {
	w.Header().Set("WWW-Authenticate", challenge)
	http.Error(w, msg, http.StatusUnauthorized)
}
