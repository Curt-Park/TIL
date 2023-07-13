package main

type Node struct {
	Val       int
	Neighbors []*Node
}

func cloneGraph(node *Node) *Node {
	var clone func(*Node, map[int]*Node) *Node
	clone = func(node *Node, m map[int]*Node) *Node {
		if node == nil {
			return nil
		}
		if _, exist := m[node.Val]; exist {
			return m[node.Val]
		}
		newNode := &Node{Val: node.Val}
		m[node.Val] = newNode
		for _, neighbor := range node.Neighbors {
			newNode.Neighbors = append(newNode.Neighbors, clone(neighbor, m))
		}
		return newNode
	}
	return clone(node, map[int]*Node{})
}
