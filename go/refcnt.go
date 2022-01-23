package main

import (
    "fmt"
    "runtime"
)

type Entity struct {
    Name string
}

var counter int = 0

func New(name string) *Entity {
    entity := Entity{name}
    counter++
    runtime.SetFinalizer(&entity, func(_ *Entity){
        counter--
    })
    return &entity
}

func main() {
    e := New("Sausage")
    fmt.Println("Entities", counter, e)
    e = New("Potato")
    fmt.Println("Entities", counter, e)
    runtime.GC()
    fmt.Println("Entities", counter, e)
    e = New("Leek")
    fmt.Println("Entities", counter, e)
    runtime.GC()
    fmt.Println("Entities", counter, e)
}
