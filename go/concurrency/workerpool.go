package concurrency

import (
	"fmt"
	"sync"
)

var wg sync.WaitGroup

func main() {
	nFib := 30
	nThread := 8 // you can see multiple threads consumes more CPU than a single thread

	jobs := make(chan int, nFib)
	results := make(chan int, nFib)
	go runWorkerPool(nThread, jobs, results)

	for i := 0; i < nFib; i++ {
		jobs <- i
	}
	close(jobs)

	for result := range results {
		fmt.Println(result)
	}
}

func runWorkerPool(n int, jobs chan int, results chan int) {
	for i := 0; i < n; i++ {
		go worker(jobs, results)
	}
	wg.Wait()
	close(results)
}

func worker(jobs chan int, results chan int) {
	wg.Add(1)
	for n := range jobs {
		results <- fib(n)
	}
	wg.Done()
}

func fib(n int) int {
	if n <= 1 {
		return n
	}
	return fib(n-1) + fib(n-2)
}
