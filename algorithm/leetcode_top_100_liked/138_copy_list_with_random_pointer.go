package main

type Node struct {
	Val    int
	Next   *Node
	Random *Node
}

func copyRandomList(head *Node) *Node {
	node, m := head, map[*Node]*Node{}
	m[nil] = nil
	for node != nil {
		m[node] = &Node{
			Val:    node.Val,
			Next:   node.Next,
			Random: node.Random,
		}
		node = node.Next
	}
	for _, node := range m {
		if node == nil {
			continue
		}
		node.Next = m[node.Next]
		node.Random = m[node.Random]
	}
	return m[head]
}
