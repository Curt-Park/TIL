// Chapter 01: a server that verifies the caller's password on every request.
//
// The user name no longer arrives on its own. It comes with a password, and the
// count is served only if the password matches the stored hash.
package main

import (
	"fmt"
	"log"
	"net/http"
	"sync"

	"golang.org/x/crypto/bcrypt"
)

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
// unknown name and a wrong password take the same time to reject. Without it
// the response time alone tells an attacker which names are real.
var decoyHash = []byte("$2a$10$mC5YwduUFPE5HzokURxBFeVvaR/0cSJ0npXFRWjpFC5zs18.Qx7dS")

var (
	mu     sync.Mutex
	counts = map[string]int{}
)

func main() {
	http.HandleFunc("GET /whoami", whoami)
	log.Fatal(http.ListenAndServe(":18080", nil))
}

func whoami(w http.ResponseWriter, r *http.Request) {
	user, password, ok := r.BasicAuth()
	if !ok {
		unauthorized(w, "missing credentials")
		return
	}

	hash, found := users[user]
	if !found {
		hash = decoyHash
	}

	// CompareHashAndPassword re-hashes the password with the salt and cost read
	// from the stored hash, then compares the two in constant time. It runs even
	// for an unknown user so that both failures cost the same.
	if err := bcrypt.CompareHashAndPassword(hash, []byte(password)); err != nil || !found {
		unauthorized(w, "invalid credentials")
		return
	}

	mu.Lock()
	counts[user]++
	count := counts[user]
	mu.Unlock()

	fmt.Fprintf(w, "%s: %d\n", user, count)
}

// unauthorized rejects a request with a challenge. RFC 9110 requires every 401
// to carry a WWW-Authenticate header telling the client how to authenticate, so
// it belongs on the wrong-password path as much as on the no-credentials one.
func unauthorized(w http.ResponseWriter, msg string) {
	w.Header().Set("WWW-Authenticate", `Basic realm="whoami"`)
	http.Error(w, msg, http.StatusUnauthorized)
}
