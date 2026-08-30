// Chapter 05: a server that keeps nothing in the page.
//
// Every value the client must carry is handed to the browser instead of to the
// page: the state that binds the login to this browser, and the session that
// follows it. The page's JavaScript never touches either one.
//
// Two services run here as before. The app is ours; the provider is the
// authorization server and the only place the password is ever sent.
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
