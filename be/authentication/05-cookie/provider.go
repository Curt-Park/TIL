package main

import (
	"crypto/hmac"
	"crypto/rand"
	"encoding/json"
	"net/http"
	"net/url"
	"sync"
	"time"

	"golang.org/x/crypto/bcrypt"
)

const (
	codeTTL    = time.Minute
	idTokenTTL = 5 * time.Minute
)

// users lives here and nowhere else. The app has no such map: that is the whole
// point of this chapter. alice's password is "wonderland", bob's is "builder".
var users = map[string][]byte{
	"alice": []byte("$2a$10$7EImLcB7G74VfPpdnIAW6O7WZPMIhyixt94t0F9vfrnLrGksG7tF2"),
	"bob":   []byte("$2a$10$4MrcNrf//Cq0jKSSvu2uq.1xOBIz6GzCDnmXc8uxy6lQEJOE91t4m"),
}

// decoyHash is compared against when the user does not exist, so that an
// unknown name and a wrong password take the same time to reject.
var decoyHash = []byte("$2a$10$mC5YwduUFPE5HzokURxBFeVvaR/0cSJ0npXFRWjpFC5zs18.Qx7dS")

// authCode is what the provider remembers between /authorize and /token. It
// binds the code to one user and to one code_challenge.
type authCode struct {
	user      string
	challenge string
	expires   time.Time
}

var (
	provMu sync.Mutex
	codes  = map[string]authCode{}
)

func providerRoutes() *http.ServeMux {
	mux := http.NewServeMux()
	mux.HandleFunc("GET /authorize", authorize)
	mux.HandleFunc("POST /token", token)
	return mux
}

func authorize(w http.ResponseWriter, r *http.Request) {
	q := r.URL.Query()

	// redirect_uri is checked against what the client registered. Without this
	// an attacker could ask the provider to deliver the code to their own site.
	if q.Get("client_id") != clientID || q.Get("redirect_uri") != redirectURI {
		http.Error(w, "unknown client", http.StatusBadRequest)
		return
	}

	// A real provider serves an HTML login and consent page here. Basic auth
	// stands in for it so that the flow can be driven with curl. Either way the
	// password arrives at the provider and nowhere else.
	user, password, ok := r.BasicAuth()
	if !ok {
		unauthorized(w, `Basic realm="provider"`, "missing credentials")
		return
	}
	hash, found := users[user]
	if !found {
		hash = decoyHash
	}
	if err := bcrypt.CompareHashAndPassword(hash, []byte(password)); err != nil || !found {
		unauthorized(w, `Basic realm="provider"`, "invalid credentials")
		return
	}

	code := rand.Text()

	provMu.Lock()
	codes[code] = authCode{
		user:      user,
		challenge: q.Get("code_challenge"),
		expires:   time.Now().Add(codeTTL),
	}
	provMu.Unlock()

	// The code goes back through the browser, so it is short-lived, single use,
	// and worthless without the code_verifier.
	back := url.Values{"code": {code}, "state": {q.Get("state")}}
	http.Redirect(w, r, q.Get("redirect_uri")+"?"+back.Encode(), http.StatusFound)
}

func token(w http.ResponseWriter, r *http.Request) {
	if r.FormValue("client_id") != clientID || r.FormValue("client_secret") != clientSecret {
		http.Error(w, "invalid client", http.StatusUnauthorized)
		return
	}

	provMu.Lock()
	c, ok := codes[r.FormValue("code")]
	delete(codes, r.FormValue("code"))
	provMu.Unlock()
	if !ok || time.Now().After(c.expires) {
		http.Error(w, "invalid grant", http.StatusBadRequest)
		return
	}

	// PKCE: only the party that sent the challenge knows the verifier behind it.
	if !hmac.Equal([]byte(challenge(r.FormValue("code_verifier"))), []byte(c.challenge)) {
		http.Error(w, "invalid code_verifier", http.StatusBadRequest)
		return
	}

	// access_token would authorize calls to the provider's own API. The app
	// does not need it here: it only wanted to know who the user is, which the
	// id_token says.
	id := signJWS([]byte(clientSecret), claims{
		Iss: issuer,
		Sub: c.user,
		Aud: clientID,
		Exp: time.Now().Add(idTokenTTL).Unix(),
	})

	w.Header().Set("Content-Type", "application/json")
	if err := json.NewEncoder(w).Encode(map[string]string{
		"access_token": rand.Text(),
		"token_type":   "Bearer",
		"id_token":     id,
	}); err != nil {
		return
	}
}

// unauthorized rejects a request with a Basic challenge. RFC 9110 requires every
// 401 to carry a WWW-Authenticate header telling the client how to authenticate.
// Only the provider still uses HTTP authentication; the app has moved to cookies.
func unauthorized(w http.ResponseWriter, challenge, msg string) {
	w.Header().Set("WWW-Authenticate", challenge)
	http.Error(w, msg, http.StatusUnauthorized)
}
