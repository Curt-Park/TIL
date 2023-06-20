package main

import "math"

func maxPathSum(root *TreeNode) int {
	maxVal := math.MinInt
	var findMaxPathSum func(*TreeNode) int
	findMaxPathSum = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		left := findMaxPathSum(node.Left)
		right := findMaxPathSum(node.Right)
		maxVal = max(maxVal, node.Val+left+right)
		return max(0, max(node.Val, max(node.Val+left, node.Val+right)))
	}
	findMaxPathSum(root)
	return maxVal
}
