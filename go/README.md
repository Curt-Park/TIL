# Materials
- https://go.dev/doc/tutorial/getting-started
- https://go.dev/doc/effective_go
- https://github.com/bvwells/go-patterns
- https://github.com/lotusirous/go-concurrency-patterns

# Install a module in Go

## 1. Write code
```go
// helloworld.go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World.")
}
```

## 2. Add the module
```bash
$ go mod init helloworld  # choose a module path
$ go install helloworld  # build and install the program
```

## 3. Execute
```bash
$ export PATH=$PATH:$(dirname $(go list -f '{{.Target}}' .))
$ helloworld
Hello, World!
```
