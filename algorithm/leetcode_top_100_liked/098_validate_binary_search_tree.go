package main

import "math"

func isValidBST0(root *TreeNode) bool {
	var validateBST func(*TreeNode, int, int) bool
	validateBST = func(node *TreeNode, min, max int) bool {
		if node == nil {
			return true
		}
		return node.Val > min && node.Val < max &&
			validateBST(node.Left, min, node.Val) &&
			validateBST(node.Right, node.Val, max)
	}
	return validateBST(root, math.MinInt64, math.MaxInt64)
}

func isValidBST1(root *TreeNode) bool {
	arr := []int{}
	var traverse func(*TreeNode)
	traverse = func(node *TreeNode) {
		if node == nil {
			return
		}
		traverse(node.Left)
		arr = append(arr, node.Val)
		traverse(node.Right)
	}
	traverse(root)
	for i := 0; i < len(arr)-1; i++ {
		if arr[i] >= arr[i+1] {
			return false
		}
	}
	return true
}
