package main

import (
	"crypto/rand"
	"crypto/subtle"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"sync"
	"time"
)

const (
	sessionTTL = 15 * time.Minute
	stateTTL   = 5 * time.Minute

	stateCookie   = "oauth_state"
	sessionCookie = "session"

	// secureCookies belongs on in any real deployment: it tells the browser to
	// withhold the cookie from plain HTTP. It is off here only because the
	// tutorial runs on http://localhost.
	secureCookies = false
)

// appSecret signs the app's own session tokens.
var appSecret = []byte("app-secret-not-for-real-use")

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
	mux.HandleFunc("GET /{$}", appIndex)
	mux.HandleFunc("GET /login", appLogin)
	mux.HandleFunc("GET /callback", appCallback)
	mux.HandleFunc("GET /whoami", appWhoami)
	mux.HandleFunc("POST /reset", appReset)
	return mux
}

func appLogin(w http.ResponseWriter, r *http.Request) {
	state := rand.Text()
	verifier := rand.Text()

	appMu.Lock()
	pendings[state] = pending{verifier: verifier, expires: time.Now().Add(stateTTL)}
	appMu.Unlock()

	// The same state leaves by two routes: in the URL below, and into this
	// browser's keeping. At /callback the two must agree. Anyone can build the
	// URL, but nobody can put a value into someone else's browser.
	setCookie(w, stateCookie, state, int(stateTTL.Seconds()))

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

	// The browser's copy decides. A callback carrying a state this browser never
	// received is somebody else's login being pushed onto this user.
	kept, err := r.Cookie(stateCookie)
	if err != nil || subtle.ConstantTimeCompare([]byte(kept.Value), []byte(q.Get("state"))) != 1 {
		http.Error(w, "state does not belong to this browser", http.StatusBadRequest)
		return
	}
	setCookie(w, stateCookie, "", -1)

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

	c, ok := verifyJWS([]byte(clientSecret), idToken)
	if !ok || c.Iss != issuer || c.Aud != clientID {
		http.Error(w, "invalid id_token", http.StatusBadGateway)
		return
	}

	// The session goes to the browser, not to the page. HttpOnly keeps it out of
	// document.cookie, so a script that gets onto the page cannot read it.
	session := signJWS(appSecret, claims{Sub: c.Sub, Exp: time.Now().Add(sessionTTL).Unix()})
	setCookie(w, sessionCookie, session, int(sessionTTL.Seconds()))
	http.Redirect(w, r, "/", http.StatusFound)
}

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
	c, ok := session(r)
	if !ok {
		// Cookies are not an HTTP authentication scheme, so there is no
		// WWW-Authenticate challenge to send. A page-based app would redirect to
		// its login instead; this one answers plainly so curl can read it.
		http.Error(w, "no session", http.StatusUnauthorized)
		return
	}

	appMu.Lock()
	counts[c.Sub]++
	count := counts[c.Sub]
	appMu.Unlock()

	fmt.Fprintf(w, "%s: %d\n", c.Sub, count)
}

// appReset exists to have something worth attacking: a request that changes
// state rather than reading it.
func appReset(w http.ResponseWriter, r *http.Request) {
	c, ok := session(r)
	if !ok {
		http.Error(w, "no session", http.StatusUnauthorized)
		return
	}

	appMu.Lock()
	delete(counts, c.Sub)
	appMu.Unlock()

	fmt.Fprintf(w, "%s: reset\n", c.Sub)
}

func session(r *http.Request) (claims, bool) {
	c, err := r.Cookie(sessionCookie)
	if err != nil {
		return claims{}, false
	}
	return verifyJWS(appSecret, c.Value)
}

// setCookie writes one cookie with the attributes this chapter is about.
// SameSite=Lax tells the browser to withhold it from requests another site
// starts, which is what makes the automatic attachment safe to rely on.
func setCookie(w http.ResponseWriter, name, value string, maxAge int) {
	http.SetCookie(w, &http.Cookie{
		Name:     name,
		Value:    value,
		Path:     "/",
		MaxAge:   maxAge,
		HttpOnly: true,
		Secure:   secureCookies,
		SameSite: http.SameSiteLaxMode,
	})
}

func appIndex(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "text/html; charset=utf-8")
	io.WriteString(w, indexHTML)
}

// indexHTML asks the page for two things the chapter claims: that JavaScript
// cannot see the session, and that the request carrying it still succeeds.
const indexHTML = `<!doctype html>
<meta charset="utf-8">
<title>05 cookie</title>
<p><a href="/login">로그인</a></p>
<p>document.cookie: <b id="c"></b></p>
<p>fetch('/whoami'): <b id="w"></b></p>
<script>
document.getElementById('c').textContent = document.cookie || '(비어 있음)'
fetch('/whoami')
  .then(r => r.text())
  .then(t => { document.getElementById('w').textContent = t.trim() })
</script>
`
