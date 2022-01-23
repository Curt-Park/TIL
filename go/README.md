# Materials

## Basics
- https://go.dev/doc/tutorial/getting-started
- https://go.dev/doc/effective_go

## Concurrency
- [Concurrency Patterns In Go](https://youtu.be/YEKjSzIwAdA)
- [GopherCon 2017: Kavya Joshi - Understanding Channels](https://youtu.be/KBZlN0izeiY)
- https://github.com/lotusirous/go-concurrency-patterns
- [Goroutine 은 어떻게 동작할까?](https://sungjunyoung.github.io/posts/how-goroutine-works/)

## Channel vs Mutex?
- [Locks versus channels in concurrent Go](https://opensource.com/article/18/7/locks-versus-channels-concurrent-go)
- [Reddit](https://www.reddit.com/r/golang/comments/m3oys6/comment/gqsbr8t/?utm_source=share&utm_medium=web2x&context=3)
- [Go Wiki](Use a sync.Mutex or a channel?)

## Design Patterns
- https://github.com/bvwells/go-patterns

# How to install a module in Go

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

# Reads

