// Chapter 02: a server that checks the password once and hands back a session
// ID for every request that follows.
//
// The password is read only at /login. From then on the client carries an ID
// the server drew and can throw away.
package main

import (
	"crypto/rand"
	"fmt"
	"log"
	"net/http"
	"strings"
	"sync"
	"time"

	"golang.org/x/crypto/bcrypt"
)

// sessionTTL bounds how long a stolen ID stays useful. A session is not a
// permanent grant: it expires whether or not anyone logs out.
const sessionTTL = 30 * time.Minute

// users maps a user name to the bcrypt hash of its password. The plaintext is
// never stored.
//
// These hashes were produced by bcrypt.GenerateFromPassword, which is what a
// signup handler would call. This server has no signup, so they are baked in as
// literals. alice's password is "wonderland", bob's is "builder".
var users = map[string][]byte{
	"alice": []byte("$2a$10$7EImLcB7G74VfPpdnIAW6O7WZPMIhyixt94t0F9vfrnLrGksG7tF2"),
	"bob":   []byte("$2a$10$4MrcNrf//Cq0jKSSvu2uq.1xOBIz6GzCDnmXc8uxy6lQEJOE91t4m"),
}

// decoyHash is compared against when the user does not exist, so that an
// unknown name and a wrong password take the same time to reject.
var decoyHash = []byte("$2a$10$mC5YwduUFPE5HzokURxBFeVvaR/0cSJ0npXFRWjpFC5zs18.Qx7dS")

type session struct {
	user    string
	expires time.Time
}

var (
	mu       sync.Mutex
	counts   = map[string]int{}
	sessions = map[string]session{}
)

func main() {
	http.HandleFunc("POST /login", login)
	http.HandleFunc("POST /logout", logout)
	http.HandleFunc("GET /whoami", whoami)
	log.Fatal(http.ListenAndServe(":18080", nil))
}

func login(w http.ResponseWriter, r *http.Request) {
	user, password, ok := r.BasicAuth()
	if !ok {
		unauthorized(w, `Basic realm="whoami"`, "missing credentials")
		return
	}

	hash, found := users[user]
	if !found {
		hash = decoyHash
	}
	if err := bcrypt.CompareHashAndPassword(hash, []byte(password)); err != nil || !found {
		unauthorized(w, `Basic realm="whoami"`, "invalid credentials")
		return
	}

	// rand.Text draws at least 128 bits from the OS random source. The ID is
	// the evidence itself, so an attacker who could guess one would not need
	// the password at all.
	//
	// The server draws it and never accepts one the client proposes. Letting a
	// client choose its own ID would let an attacker plant a value it already
	// knows and wait for the victim to log in under it: session fixation.
	id := rand.Text()

	mu.Lock()
	sessions[id] = session{user: user, expires: time.Now().Add(sessionTTL)}
	mu.Unlock()

	fmt.Fprintln(w, id)
}

func logout(w http.ResponseWriter, r *http.Request) {
	id, ok := bearer(r)
	if !ok {
		unauthorized(w, `Bearer realm="whoami"`, "missing session")
		return
	}

	// Forgetting the ID is all it takes to revoke it, and nothing else is
	// touched: the account stands and the user's other sessions stand. Revoking
	// a password means dropping the stored hash, which locks the legitimate
	// user out until they choose a new one.
	mu.Lock()
	delete(sessions, id)
	mu.Unlock()

	w.WriteHeader(http.StatusNoContent)
}

func whoami(w http.ResponseWriter, r *http.Request) {
	id, ok := bearer(r)
	if !ok {
		unauthorized(w, `Bearer realm="whoami"`, "missing session")
		return
	}

	s, ok := lookup(id)
	if !ok {
		unauthorized(w, `Bearer realm="whoami", error="invalid_token"`, "invalid session")
		return
	}

	mu.Lock()
	counts[s.user]++
	count := counts[s.user]
	mu.Unlock()

	fmt.Fprintf(w, "%s: %d\n", s.user, count)
}

func bearer(r *http.Request) (string, bool) {
	return strings.CutPrefix(r.Header.Get("Authorization"), "Bearer ")
}

// lookup returns the session behind an ID, dropping it if it has expired. An ID
// the server does not remember is worth nothing, which is the whole point.
func lookup(id string) (session, bool) {
	mu.Lock()
	defer mu.Unlock()

	s, ok := sessions[id]
	if !ok {
		return session{}, false
	}
	if time.Now().After(s.expires) {
		delete(sessions, id)
		return session{}, false
	}
	return s, true
}

// unauthorized rejects a request with a challenge. RFC 9110 requires every 401
// to carry a WWW-Authenticate header telling the client how to authenticate.
func unauthorized(w http.ResponseWriter, challenge, msg string) {
	w.Header().Set("WWW-Authenticate", challenge)
	http.Error(w, msg, http.StatusUnauthorized)
}
