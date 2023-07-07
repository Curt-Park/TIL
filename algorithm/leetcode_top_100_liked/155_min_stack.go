package main

type Node struct {
	Val int
	Min int
}

type MinStack struct {
	Stack []Node
}

func Constructor() MinStack {
	return MinStack{Stack: []Node{}}
}

func (this *MinStack) Push(val int) {
	var minVal int
	if len(this.Stack) == 0 {
		minVal = val
	} else {
		minVal = this.GetMin()
	}
	node := Node{Val: val, Min: min(minVal, val)}
	this.Stack = append(this.Stack, node)
}

func (this *MinStack) Pop() {
	this.Stack = this.Stack[:len(this.Stack)-1]
}

func (this *MinStack) Top() int {
	return this.Stack[len(this.Stack)-1].Val
}

func (this *MinStack) GetMin() int {
	return this.Stack[len(this.Stack)-1].Min
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
