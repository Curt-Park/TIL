package main

type DoublyListNode struct {
	Key  int
	Val  int
	Prev *DoublyListNode
	Next *DoublyListNode
}

type LRUCache struct {
	Head *DoublyListNode
	Tail *DoublyListNode
	M    map[int]*DoublyListNode
	Cap  int
}

func Constructor(capacity int) LRUCache {
	head := &DoublyListNode{}
	tail := &DoublyListNode{}
	head.Next = tail
	tail.Prev = head
	return LRUCache{
		Head: head,
		Tail: tail,
		M:    map[int]*DoublyListNode{},
		Cap:  capacity,
	}
}

func (this *LRUCache) Get(key int) int {
	if _, exist := this.M[key]; !exist {
		return -1
	}
	node := this.M[key]
	node.Prev.Next = node.Next
	node.Next.Prev = node.Prev
	this.Add(node)
	return node.Val
}

func (this *LRUCache) Put(key int, value int) {
	if this.Get(key) != -1 {
		this.Head.Next.Val = value
		return
	}
	node := &DoublyListNode{Key: key, Val: value}
	this.Add(node)
	this.M[key] = node
	if len(this.M) > this.Cap {
		node = this.Tail.Prev
		node.Prev.Next = this.Tail
		this.Tail.Prev = node.Prev
		delete(this.M, node.Key)
	}
}

func (this *LRUCache) Add(node *DoublyListNode) {
	node.Prev = this.Head
	node.Next = this.Head.Next
	this.Head.Next = node
	node.Next.Prev = node
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
