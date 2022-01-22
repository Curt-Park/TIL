// https://go-tour-ko.appspot.com/flowcontrol
package main

import (
	"fmt"
	"math"
	"runtime"
	"time"
)

func loop1(from, to int) int {
	sum := 0
	for i := from; i <= to; i++ {
		sum += i
	}
	return sum
}

func loop2(upperBound int) int {
	sum := 1
	// init and post processing can be omitted
	for sum <= upperBound {
		sum += sum
	}
	return sum
}

func loop3(upperBound int) int {
	sum := 1
	// ; can be omitted as well
	// the following is same as while as a result
	for sum <= upperBound {
		sum += sum
	}
	return sum
}

func infinitLoop() {
	for {
	}
}

func pow1(x, n, lim float64) float64 {
	// v is availbe in the scope of if
	if v := math.Pow(x, n); v < lim {
		return v
	}
	return lim
}

func pow2(x, n, lim float64) float64 {
	if v := math.Pow(x, n); v < lim {
		return v
	} else {
		fmt.Printf("%g >= %g\n", v, lim)
	}
	// can't use v here though
	return lim
}

func sqrt1(x float64) string {
	if x < 0 {
		return sqrt1(-x) + "i"
	}
	return fmt.Sprint(math.Sqrt(x))
}

func sqrt2(x float64) float64 {
	z := 1.0
	for i := 0; i < 10; i++ {
		next_z := z - (z*z-x)/(2*z)
		if math.Abs(z-next_z) < 1e-6 {
			break
		}
		z = next_z
	}
	return z
}

func checkOS() {
	fmt.Print("Go runs on ")
	switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("OS X.")
	case "linux":
		fmt.Println("Lunux.")
	default:
		// freebsd, openbsd,
		// plan9, windows...
		fmt.Printf("%s.\n", os)
	}
}

func checkSaturday() {
	fmt.Print("When's Saturday? ")
	today := time.Now().Weekday()
	switch time.Saturday {
	case today + 0:
		fmt.Println("Today.")
	case today + 1:
		fmt.Println("Tomorrow.")
	case today + 2:
		fmt.Println("In two days.")
	default:
		fmt.Println("Too far away.")
	}
}

func noConditionSwitch() {
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("Good morning!")
	case t.Hour() < 17:
		fmt.Println("Good afternoon!")
	default:
		fmt.Println("Good evening.")
	}
}

// defer delays execution until the scope ends
func deferPractice() {
	defer fmt.Println("world")
	fmt.Print("hello ")
}

// defer calls are stacked
func deferInStack() {
	fmt.Print("counting ")

	for i := 0; i < 10; i++ {
		defer fmt.Printf("%d ", i)
	}
}

func main() {
	fmt.Println(loop1(1, 50))
	fmt.Println(loop2(1000))
	fmt.Println(loop3(1000))
	fmt.Println(pow1(3, 2, 10), pow1(3, 3, 20))
	fmt.Println(pow2(3, 2, 10), pow2(3, 3, 20))
	fmt.Println(sqrt1(2), sqrt1(3), sqrt1(4))
	fmt.Println(sqrt2(2), sqrt2(3), sqrt2(4))
	checkOS()
	checkSaturday()
	noConditionSwitch()
	deferPractice()
	deferInStack()
}
