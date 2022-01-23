package concurrency

import (
	"fmt"
	"time"
)

var msgs = make(chan int)
var done = make(chan bool)

func main() {
	go produce(5)
	go consume()
	<-done
	fmt.Println("Done")
}

func produce(n int) {
	for i := 0; i < n; i++ {
		time.Sleep(time.Second) // production time
		msgs <- i               // wait until consumed
		fmt.Println("Produced", i)
	}
	close(msgs) // channel must be closed by producer
}

func consume() {
	for msg := range msgs {
		fmt.Println("Consumed", msg)
	}
	done <- true // consumed all msgs
}
