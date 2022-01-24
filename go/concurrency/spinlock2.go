package main

import (
	"fmt"
	"runtime"
	"strconv"
	"strings"
	"sync"
	"sync/atomic"
)

type spinLock struct {
	owner  int
	count  int
	locked uint32
}

func (sl *spinLock) Lock() {
	me := GetGoroutineId()
	// If the current thread has acquired the lock, the number of threads increases by one, and then returns
	if sl.owner == me {
		sl.count++
		return
	}
	// If the lock is not acquired, spin through CAS
	for !atomic.CompareAndSwapUint32(&sl.locked, 0, 1) {
		runtime.Gosched()
	}
}

func (sl *spinLock) Unlock() {
	if sl.owner != GetGoroutineId() {
		panic("illegalMonitorStateError")
	}
	// if greater than 0, it means that the current thread has acquired the lock many times,
	// and the release lock is simulated by subtracting count from one.
	if sl.count > 0 {
		sl.count--
		// If count== 0, the lock can be released,
		// which ensures that the number of acquisitions of the lock is the same as the number of releases of the lock.
	} else {
		atomic.StoreUint32(&sl.locked, 0)
	}
}

func GetGoroutineId() int {
	defer func() {
		if err := recover(); err != nil {
			fmt.Println("panic recover:panic info:%v", err)
		}
	}()

	var buf [64]byte
	n := runtime.Stack(buf[:], false)
	idField := strings.Fields(strings.TrimPrefix(string(buf[:n]), "goroutine "))[0]
	id, err := strconv.Atoi(idField)
	if err != nil {
		panic(fmt.Sprintf("cannot get goroutine id: %v", err))
	}
	return id
}

func NewSpinLock2() sync.Locker {
	var lock spinLock
	return &lock
}
