// Chapter 04: a server that never sees a password.
//
// Two services run here. The app is ours; it holds no passwords at all. The
// provider is the authorization server, and it is the only place the password
// is ever sent. They share a process so that `go run .` starts both, but they
// are independent services and would be deployed as such.
package main

import (
	"log"
	"net/http"
)

const (
	appAddr      = ":18080"
	providerAddr = ":19090"

	// The app registered with the provider and received these. clientSecret
	// authenticates the app itself when it redeems a code, and also signs the
	// id_token the provider hands back.
	clientID     = "til-authentication"
	clientSecret = "client-secret-shared-with-the-provider"

	// redirectURI is registered with the provider in advance. The provider
	// sends the user back only to this address, so an attacker cannot redirect
	// the code somewhere else.
	redirectURI = "http://localhost:18080/callback"
	issuer      = "http://localhost:19090"
)

func main() {
	go func() { log.Fatal(http.ListenAndServe(providerAddr, providerRoutes())) }()
	log.Fatal(http.ListenAndServe(appAddr, appRoutes()))
}
