package main

import (
	"fmt"
	"time"
)

func channel() {
	s := []int{7, 2, 8, -9, 4, 0}
	c := make(chan int) // channel
	go sum(s[:len(s)/2], c)
	go sum(s[len(s)/2:], c)
	x, y := <-c, <-c // receive from c

	fmt.Println(x, y, x+y)
}

func bufferedChannel() {
	ch := make(chan int, 2)
	ch <- 1
	ch <- 2
	// ch <- 3 raises error
	fmt.Print(<-ch, " ")
	fmt.Println(<-ch)
	// fmt.Println(<-ch) raises error
}

func rangeAndClose() {
	c := make(chan int, 10)
	go fibonacci(cap(c), c)
	for i := range c {
		fmt.Print(i, " ")
	}
	fmt.Println()
}

func defaultSelection() {
	// create channels
	tick := time.Tick(100 * time.Millisecond)
	boom := time.After(500 * time.Millisecond)
	for {
		select {
		case <-tick:
			fmt.Print("tick")
		case <-boom:
			fmt.Println("BOOM!")
			return
		default: // execute when other cases are not ready
			fmt.Print(".")
			time.Sleep(50 * time.Millisecond)
		}
	}
}

func main() {
	channel()
	bufferedChannel()
	rangeAndClose()
	defaultSelection()
}

/* Helper functions */

func sum(s []int, c chan int) {
	sum := 0
	for _, v := range s {
		sum += v
	}
	c <- sum
}

func fibonacci(n int, c chan int) {
	x, y := 0, 1
	for i := 0; i < n; i++ {
		c <- x
		x, y = y, x+y
	}
	close(c) // v, ok <- ch tells the channel is closed
}
