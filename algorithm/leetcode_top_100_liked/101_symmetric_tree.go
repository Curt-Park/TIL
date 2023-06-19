package main

func isSymmetric(root *TreeNode) bool {
	var validate func(*TreeNode, *TreeNode) bool
	validate = func(node1 *TreeNode, node2 *TreeNode) bool {
		if node1 == nil && node2 == nil {
			return true
		} else if node1 == nil || node2 == nil {
			return false
		}
		return node1.Val == node2.Val && validate(node1.Left, node2.Right) &&
			validate(node1.Right, node2.Left)
	}
	return validate(root.Left, root.Right)
}
