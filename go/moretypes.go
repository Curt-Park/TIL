package main

import "fmt"

type Vertex struct {
	X int
	Y int
	// or X, Y int
}

func pointer1() {
	i, j := 42, 2701

	p := &i // var p *int
	fmt.Print(*p, " ")
	*p = 21 // change i's value
	fmt.Print(i, " ")

	p = &j
	*p = *p / 37 // change j's value
	fmt.Print(j, "\n")
}

func structField() {
	v := Vertex{1, 2}
	v.X = 4
	fmt.Println(v)
}

func pointerToStructs() {
	v := Vertex{1, 2}
	p := &v
	p.X = 1e9 // same as `(*p).x`
	(*p).Y = 10
	fmt.Println(v)
}

func structLiterals() {
	var (
		v1 = Vertex{1, 2}
		v2 = Vertex{X: 1} // Y:0 is implicit
		v3 = Vertex{}     // X:0 and Y:0
		p  = &Vertex{1, 2}
	)
	fmt.Println(v1, p, v2, v3)
}

func sliceLiterals() {
    q := []int{2, 3, 5, 7, 11, 13}
    fmt.Println(q)

    r := []bool{true, false, true, true, false, true}
    fmt.Println(r)

    s := []struct {
        i int
        b bool
    }{
        {2, true},
        {3, false},
        {5, true},
        {7, true},
    }
    fmt.Println(s)
}

func arrays() {
	var a [2]string
	a[0] = "Hello"
	a[1] = "World"
	fmt.Print(a[0], a[1], " ")
	fmt.Print(a, " ")

	primes := [6]int{2, 3, 5, 7, 11, 13}
	fmt.Println(primes)
}

func slices() {
    primes := [6]int{2, 3, 5, 7, 11, 13}
    var s []int = primes[1:4]
    fmt.Println(s)
}

func main() {
	pointer1()
	fmt.Println(Vertex{1, 2})
	structField()
	pointerToStructs()
	structLiterals()
	arrays()
    slices()
    sliceLiterals()
}
