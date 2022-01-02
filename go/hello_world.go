// https://go-tour-ko.appspot.com/basics
// `$ go run hello_world.go` compiles and runs the package.
// `$ go fmt hello_world.go` checkes the formats and modifies if needed
package main

// multiple lines for imports possible as well
// however, the following "factored" import is preferred
import (
	// What was the reason behind using quotes in Go's import statements?
	// https://bit.ly/3HxlHRj
	"fmt"
	"math"
	"math/cmplx"
	"math/rand"
	"time"
)

// add returns the summation of the integer inputs
// why types are behind variables: https://go.dev/blog/declaration-syntax
// shortly, it has benefits for better readability w.r.t. function pointers.
func add(x, y int) int {
	return x + y
}

// swap the two input strings
func swap(x, y string) (string, string) {
	return y, x
}

// return values possibly have names for description
func split(sum int) (x, y int) {
	x = sum % 10
	y = sum - x
	return // naked return
}

// variables in package
var c, python, java bool // var names type

// multiple variables with types and initial values
var (
	ToBe   bool       = false
	MaxInt uint64     = 1<<64 - 1
	z      complex128 = cmplx.Sqrt(-5 + 12i)
)

// numeric constants
// it takes a proper type from the context
const (
	Big   = 1.0 << 100
	Small = Big >> 99
)

func main() {
	fmt.Println("Hello World!")
	fmt.Println("The time is", time.Now())
	fmt.Println("Random generated number is", rand.Intn(100))
	// https://pkg.go.dev/fmt#hdr-Printing
	fmt.Printf("Square root of 7 is %g.\n", math.Sqrt(7))
	// fmt.Println(math.pi) doesn't work
	// for exports, Go uses names that starts with a capital letter
	fmt.Println(math.Pi)
	// call the user defined function
	fmt.Println(add(1, 2))

	hello, world := swap("world!", "hello")
	fmt.Println(hello, world)

	fmt.Println(split(128))

	// variable in function
	var i int // initial value is 0
	fmt.Println(i, c, python, java)

	// variables with initial values
	// the types can be omitted with initialization
	var c, python, java = true, false, "no!"
	fmt.Println(c, python, java)

	// := binds the types with initial values
	// this can be used only in functions
	i, j := 1, 2
	golang, erlang, rust := true, false, "no!"
	// `c, python, java := true, false, "no!"` not allowed
	fmt.Println(i, j, golang, erlang, rust)

	fmt.Printf("Type: %T Value: %v\n", ToBe, ToBe)
	fmt.Printf("Type: %T Value: %v\n", MaxInt, MaxInt)
	fmt.Printf("Type: %T Value: %v\n", z, z)

	// type casting
	x, y := 3, 4
	f := math.Sqrt(float64(x*x + y*y))
	z := uint(f)
	fmt.Println(x, y, z)

	// inference type
	k := i
	fmt.Println(k)

	// constant values
	// it inferences the type and binds value with `=`
	const World = "世界"
	fmt.Println("Hello", World)

	// check the numeric constants' types
	// fmt.Printf("%T %v\n", Big, Big)  // overflow error!
	fmt.Printf("%T %v\n", Small, Small)
}
