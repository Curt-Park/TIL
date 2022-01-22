package main

import (
	"fmt"
	"math"
)

// Interfaces
type Operators interface {
	Abs() float64
	Scale(float64)
}

// Receiver for non-struct types
type MyFloat float64

// (f MyFloat): value receiver copies the value
// (f *MyFloat): Point receiver refers the value
func (f *MyFloat) Abs() float64 {
	if *f < 0 {
		return float64(-*f)
	}
	return float64(*f)
}

func (f *MyFloat) Scale(s float64) {
	*f *= MyFloat(s)
}

// Receiver for struct types
type Vertex struct {
	X, Y float64
}

func (v *Vertex) Abs() float64 {
	return math.Sqrt(float64(v.X*v.X + v.Y*v.Y))
}

func (v *Vertex) Scale(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}

// Exercise: Errors
type ErrNegativeSqrt float64

func (e ErrNegativeSqrt) Error() string {
	return fmt.Sprintf("cannot Sqrt negative number: %f", e)
}
func Sqrt(x float64) (float64, error) {
	if x < 0 {
		return x, ErrNegativeSqrt(x)
	}
	return math.Sqrt(x), nil
}

func main() {
	// Receiver for non-struct types
	f := MyFloat(-math.Sqrt2)
	fmt.Println(f.Abs())

	// Receiver for struct types
	v := Vertex{3, 4}
	v.Scale(10)
	fmt.Println(v.Abs())

	// Interface
	var a Operators
	a = &f
	fmt.Println(a.Abs())
	a = &v
	fmt.Println(a.Abs())

	// Empty Interface
	// empty interface may hold values of any type
	var i interface{}
	describe(i)
	i = 42
	describe(i)
	i = "hello"
	describe(i)

	// Type Assertions
	// now a holds a Vertex pointer
	t := a.(*Vertex)
	fmt.Println(t)
	t, ok := a.(*Vertex)
	fmt.Println(t, ok)
	fa, ok := a.(*MyFloat)
	fmt.Println(fa, ok)

	// Type Switches
	switch a.(type) {
	case *Vertex:
		fmt.Println("Vertex Pointer")
	case *MyFloat:
		fmt.Println("MyFloat Pointer")
	default:
		fmt.Println("Otherwise")
	}

	// Excercise: Errors
	fmt.Println(Sqrt(2))
	fmt.Println(Sqrt(-2)) // raise error
}

// Helper Functions
func describe(i interface{}) {
	fmt.Printf("(%v, %T)\n", i, i)
}
