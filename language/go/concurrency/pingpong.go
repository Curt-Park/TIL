package main

import (
	"fmt"
	"time"
)

type Ball struct {
	hits int
}

func player(name string, table chan *Ball) {
	for {
		ball := <-table
		ball.hits++
		fmt.Printf("%s %d\n", name, ball.hits)
		time.Sleep(100 * time.Millisecond)
		table <- ball
	}
}

func main() {
	table := make(chan *Ball)

	go player("ping", table)
	go player("pong", table)
	table <- new(Ball)
	time.Sleep(time.Second)
	<-table
	panic("show me the stack")
}
