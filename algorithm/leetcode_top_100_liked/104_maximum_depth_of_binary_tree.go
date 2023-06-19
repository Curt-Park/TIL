package main

func maxDepth(root *TreeNode) int {
	var dfs func(*TreeNode, int) int
	dfs = func(node *TreeNode, lev int) int {
		if node == nil {
			return lev - 1
		}
		return max(dfs(node.Left, lev+1), dfs(node.Right, lev+1))
	}
	return dfs(root, 1)
}
