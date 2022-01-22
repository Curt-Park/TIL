package main

import "fmt"

func main() {
	nFib := 50
	nThread := 8 // you can see multiple threads consumes more CPU than a single thread

	jobs := make(chan int, nFib)
	results := make(chan int, nFib)
	runWorkerPool(nThread, jobs, results)

	for i := 0; i < nFib; i++ {
		jobs <- i
	}
	close(jobs)

	for j := 0; j < nFib; j++ {
		fmt.Println(<-results)
	}
}

func runWorkerPool(n int, jobs chan int, results chan int) {
	for i := 0; i < n; i++ {
		go worker(jobs, results)
	}
}

func worker(jobs chan int, results chan int) {
	for n := range jobs {
		results <- fib(n)
	}
}

func fib(n int) int {
	if n <= 1 {
		return n
	}
	return fib(n-1) + fib(n-2)
}
