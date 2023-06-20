package main

func flatten(root *TreeNode) {
	var construct func(*TreeNode) *TreeNode
	construct = func(node *TreeNode) *TreeNode {
		if node == nil || node.Left == nil && node.Right == nil {
			return node
		}
		left := construct(node.Left)
		right := construct(node.Right)
		if left != nil {
			left.Right = node.Right
			node.Right = node.Left
			node.Left = nil
		}
		if right != nil {
			return right
		}
		return left
	}
	construct(root)
}
