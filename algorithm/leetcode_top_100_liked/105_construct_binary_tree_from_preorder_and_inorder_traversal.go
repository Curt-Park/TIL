package main

func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 {
		return nil
	}
	node, pivot := &TreeNode{Val: preorder[0]}, 0
	for inorder[pivot] != preorder[0] {
		pivot++
	}
	node.Left = buildTree(preorder[1:pivot+1], inorder[:pivot])
	node.Right = buildTree(preorder[pivot+1:], inorder[pivot+1:])
	return node
}
