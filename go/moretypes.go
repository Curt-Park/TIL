package main

import (
    "fmt"
    "math"
)

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

func sliceDefaults() {
    s := []int{2, 3, 5, 7, 11, 13}
    s = s[1:4]
    fmt.Print(s, " ")

    s = s[2:]
    fmt.Print(s, " ")

    s = s[1:]
    fmt.Println(s)
}

func sliceLengthCapacity() {
    s := []int{2, 3, 5, 7, 11, 13}
    fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)

	// Slice the slice to give it zero length.
	s = s[:0]
    fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)

	// Extend its length.
	s = s[:4]
    fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)

	// Drop its first two values.
	s = s[2:]
    fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}

func createSliceWithMake() {
    a := make([]int, 5)
    fmt.Printf("a len=%d cap=%d %v\n", len(a), cap(a), a)
}

func appendToSlice() {
    var s []int
    fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)

    s = append(s, 1)
    fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)

    s = append(s, 2, 3, 4)
    fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}

func ranges() {
    var pow = []int{1, 2, 4, 8, 16, 32, 64, 128}
    // the following expressions are possible
    // for _, v := pow
    // for i, _ := pow
    // i := range pow
    for i, v := range pow {
        fmt.Printf("2**%d = %d\n", i, v)
    }
}

func maps() {
    type Vertex struct {
        Lat, Long float64
    }
    var m map[string]Vertex
    m = make(map[string]Vertex)
    m["Bell Labs"] = Vertex{
        40.68433, -74.39967,
    }
    fmt.Println(m)
    fmt.Println(m["Bell Labs"])
}

func mutateMaps() {
    m := make(map[string]int)
    m["Answer"] = 42
    fmt.Println("The value:", m["Answer"])

    m["Answer"] = 48
    fmt.Println("The value:", m["Answer"])

    delete(m, "Answer")
    fmt.Println("The value:", m["Answer"])

    v, ok := m["Answer"]
    fmt.Println("The value", v, "Present?", ok)
}

func functionValues() {
    hypot := func(x, y float64) float64 {
        return math.Sqrt(x*x + y*y)
    }
    fmt.Println(hypot(5, 12))
}

func adder() func(int) int {
    sum := 0
    return func(x int) int {
        sum += x
        return sum
    }
}

func functionClosures() {
    pos, neg := adder(), adder()
    for i := 0; i < 10; i++ {
        fmt.Println(
            pos(i),
            neg(-2*i),
        )
    }
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
    sliceDefaults()
    sliceLengthCapacity()
    createSliceWithMake()
    appendToSlice()
    ranges()
    maps()
    mutateMaps()
    functionValues()
    functionClosures()
}
