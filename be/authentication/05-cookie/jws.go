package main

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/base64"
	"encoding/json"
	"strings"
	"time"
)

// claims covers both tokens in this chapter: the id_token the provider issues
// about the user, and the session token the app issues for itself. The app's
// own token leaves iss and aud empty.
type claims struct {
	Iss string `json:"iss,omitempty"`
	Sub string `json:"sub"`
	Aud string `json:"aud,omitempty"`
	Exp int64  `json:"exp"`
}

func signJWS(secret []byte, c claims) string {
	header := encode([]byte(`{"alg":"HS256","typ":"JWT"}`))
	body, err := json.Marshal(c)
	if err != nil {
		panic(err)
	}

	signed := header + "." + encode(body)
	return signed + "." + encode(mac(secret, signed))
}

// verifyJWS returns the claims of a token that is both authentic and unexpired.
func verifyJWS(secret []byte, token string) (claims, bool) {
	i := strings.LastIndex(token, ".")
	if i < 0 {
		return claims{}, false
	}
	signed, sig := token[:i], token[i+1:]

	got, err := base64.RawURLEncoding.DecodeString(sig)
	if err != nil || !hmac.Equal(got, mac(secret, signed)) {
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

func mac(secret []byte, signed string) []byte {
	h := hmac.New(sha256.New, secret)
	h.Write([]byte(signed))
	return h.Sum(nil)
}

func encode(b []byte) string {
	return base64.RawURLEncoding.EncodeToString(b)
}

func challenge(verifier string) string {
	sum := sha256.Sum256([]byte(verifier))
	return encode(sum[:])
}
