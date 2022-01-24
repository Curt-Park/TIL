// https://github.com/lotusirous/go-concurrency-patterns/blob/main/3-generator/main.go
package main

import (
	"fmt"
	"math/rand"
	"time"
)

func boring(msg string) chan string {
	c := make(chan string)

	go func() {
		for i := 0; i < 10; i++ {
			c <- fmt.Sprintf("%s %d", msg, i)
			time.Sleep(time.Duration(rand.Intn(1e3)) * time.Millisecond)
		}

		close(c)
	}()

	return c
}

func main() {
	joe := boring("Joe")
	ahn := boring("Ahn")

	for i := 0; i < 10; i++ {
		fmt.Println(<-joe)
		fmt.Println(<-ahn)
	}

	fmt.Println("Done")
}
