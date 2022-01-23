package main

import (
	"runtime"
	"sync/atomic"
)

type SpinLock struct {
	locked uint32
}

func (sl *SpinLock) Lock() {
	for !atomic.CompareAndSwapUint32(&sl.locked, 0, 1) {
		runtime.Gosched()
	}
}

func (sl *SpinLock) Unlock() {
	atomic.StoreUint32(&sl.locked, 0)
}

func (sl *SpinLock) String() string {
	if atomic.LoadUint32(&sl.locked) == 1 {
		return "Locked"
	}
	return "Unlocked"
}
