// Chapter 00: a server that counts requests per user, with no way to verify
// who that user is.
//
// Unix whoami reports the user the system has already authenticated. This one
// just repeats back whatever the caller put in the header. Chapter 01 is where
// the claim finally gets verified.
package main

import (
	"fmt"
	"log"
	"net/http"
	"sync"
)

// counts tracks how many requests each user has made. A plain map is not safe
// for concurrent use, and every request runs in its own goroutine, so access
// is guarded by a mutex.
//
// The map lives in memory: it is lost on restart and is not shared between
// instances. That limitation is the subject of chapter 02.
var (
	mu     sync.Mutex
	counts = map[string]int{}
)

func main() {
	http.HandleFunc("GET /whoami", whoami)
	log.Fatal(http.ListenAndServe(":18080", nil))
}

func whoami(w http.ResponseWriter, r *http.Request) {
	user := r.Header.Get("X-User")
	if user == "" {
		http.Error(w, "missing X-User header", http.StatusBadRequest)
		return
	}

	mu.Lock()
	counts[user]++
	count := counts[user]
	mu.Unlock()

	fmt.Fprintf(w, "%s: %d\n", user, count)
}
