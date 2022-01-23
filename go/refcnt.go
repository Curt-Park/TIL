/*
Go에서는 Stack과 Heap 메모리 구분 없이 모든 변수는 Reference 기반으로 생명주기가 결정됨.

```
func New() *int32 {
    var a int32
    return &a

}

// outside the function New()
a := New()
```

C언어라면 New()가 끝나는 시점에 변수 a의 생명주기가 끝나겠지만,
Golang에서는 `a := New()`에 의해 변수 a에 대한 reference가 발생하므로 `New()`가 종료된 이후에도 a는 여전히 살아있게 됨.
반면 포인터가 아닌 값을 반환하는 경우 반환시 값의 복사가 일어나므로 `New()`가 종료된 시점에는 New 안에서 선언한 변수 a의 생명도 끝남.

```
func New() int32 {
    var a int32
    return a

}

// outside the function New()
a := New()
```

- 참고1: https://stackoverflow.com/questions/13308955/how-to-keep-track-of-the-count-of-instances-of-a-type
- 참고2: https://go.dev/doc/faq#stack_or_heap
*/

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

/*
$ go run refcnt.go
Entities 1 &{Sausage}
Entities 2 &{Potato}
Entities 1 &{Potato}
Entities 2 &{Leek}
Entities 1 &{Leek}
*/
