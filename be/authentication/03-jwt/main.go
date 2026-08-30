// Chapter 03: a server that remembers nothing.
//
// Instead of an ID that points at stored state, the client carries the state
// itself: a token holding the user name, signed so that it cannot be altered.
package main

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"strings"
	"sync"
	"time"

	"golang.org/x/crypto/bcrypt"
)

// tokenTTL is shorter than the session lifetime of the previous chapter. A
// token cannot be withdrawn once issued, so its lifetime is the only bound on
// how long a stolen one stays useful.
const tokenTTL = 15 * time.Minute

// secret signs and verifies every token. A real service would load this from
// configuration rather than source. Replacing it invalidates every token at
// once, which is the only revocation this design has.
var secret = []byte("tutorial-secret-not-for-real-use")

// users maps a user name to the bcrypt hash of its password. alice's password
// is "wonderland", bob's is "builder".
var users = map[string][]byte{
	"alice": []byte("$2a$10$7EImLcB7G74VfPpdnIAW6O7WZPMIhyixt94t0F9vfrnLrGksG7tF2"),
	"bob":   []byte("$2a$10$4MrcNrf//Cq0jKSSvu2uq.1xOBIz6GzCDnmXc8uxy6lQEJOE91t4m"),
}

// decoyHash is compared against when the user does not exist, so that an
// unknown name and a wrong password take the same time to reject.
var decoyHash = []byte("$2a$10$mC5YwduUFPE5HzokURxBFeVvaR/0cSJ0npXFRWjpFC5zs18.Qx7dS")

// claims is the token payload. It is signed, not encrypted: anyone holding the
// token can read it.
type claims struct {
	Sub string `json:"sub"`
	Exp int64  `json:"exp"`
}

var (
	mu     sync.Mutex
	counts = map[string]int{}
)

func main() {
	http.HandleFunc("POST /login", login)
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

	// Nothing is written down. The token is handed over and forgotten.
	fmt.Fprintln(w, issue(user))
}

func whoami(w http.ResponseWriter, r *http.Request) {
	token, ok := strings.CutPrefix(r.Header.Get("Authorization"), "Bearer ")
	if !ok {
		unauthorized(w, `Bearer realm="whoami"`, "missing token")
		return
	}

	c, ok := verifyActive(token)
	if !ok {
		unauthorized(w, `Bearer realm="whoami", error="invalid_token"`, "invalid token")
		return
	}

	mu.Lock()
	counts[c.Sub]++
	count := counts[c.Sub]
	mu.Unlock()

	fmt.Fprintf(w, "%s: %d\n", c.Sub, count)
}

// issue builds a JWS compact serialization: three base64url segments joined by
// dots, where the third is an HMAC over the first two.
func issue(user string) string {
	header := encode([]byte(`{"alg":"HS256","typ":"JWT"}`))
	body, err := json.Marshal(claims{Sub: user, Exp: time.Now().Add(tokenTTL).Unix()})
	if err != nil {
		panic(err)
	}

	signed := header + "." + encode(body)
	return signed + "." + encode(mac(signed))
}

// verifyActive returns the claims of a token that is both authentic and
// unexpired. Either check failing means the token is worth nothing, so the two
// live together and no handler can accidentally honour one without the other.
func verifyActive(token string) (claims, bool) {
	i := strings.LastIndex(token, ".")
	if i < 0 {
		return claims{}, false
	}
	signed, sig := token[:i], token[i+1:]

	// The algorithm is never read from the token. It is fixed at HMAC-SHA256
	// here, so a token announcing "alg":"none" gains nothing: its signature is
	// still checked against a MAC only the holder of the secret can produce.
	got, err := base64.RawURLEncoding.DecodeString(sig)
	if err != nil || !hmac.Equal(got, mac(signed)) {
		return claims{}, false
	}

	_, body, ok := strings.Cut(signed, ".")
	if !ok {
		return claims{}, false
	}
	raw, err := base64.RawURLEncoding.DecodeString(body)
	if err != nil {
		return claims{}, false
	}

	var c claims
	if err := json.Unmarshal(raw, &c); err != nil {
		return claims{}, false
	}
	if time.Now().Unix() >= c.Exp {
		return claims{}, false
	}
	return c, true
}

func mac(signed string) []byte {
	h := hmac.New(sha256.New, secret)
	h.Write([]byte(signed))
	return h.Sum(nil)
}

func encode(b []byte) string {
	return base64.RawURLEncoding.EncodeToString(b)
}

// unauthorized rejects a request with a challenge. RFC 9110 requires every 401
// to carry a WWW-Authenticate header telling the client how to authenticate.
func unauthorized(w http.ResponseWriter, challenge, msg string) {
	w.Header().Set("WWW-Authenticate", challenge)
	http.Error(w, msg, http.StatusUnauthorized)
}
