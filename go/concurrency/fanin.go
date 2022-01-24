package main

import (
	"fmt"
	"math/rand"
	"time"
)

func boring(msg string) chan string {
	c := make(chan string)
	go func() {
		for i := 0; ; i++ {
			c <- fmt.Sprintf("%s %d", msg, i)
			time.Sleep(time.Duration(rand.Intn(1e3)) * time.Millisecond)
		}
	}()
	return c
}

func fanIn(cs ...chan string) chan string {
	c := make(chan string)
	for _, ci := range cs {
		go func(ci chan string) {
			for {
				c <- <-ci
			}
		}(ci)
	}
	return c
}

func main() {
	c := fanIn(boring("Joe"), boring("Ahn"))

	for i := 0; i < 5; i++ {
		fmt.Println(<-c)
	}

	fmt.Println("done")
}
