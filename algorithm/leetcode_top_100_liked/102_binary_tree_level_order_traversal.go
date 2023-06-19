package main

func levelOrder(root *TreeNode) [][]int {
	ans, queue := [][]int{}, []*TreeNode{}
	if root != nil {
		queue = append(queue, root)
	}
	for len(queue) > 0 {
		ans = append(ans, []int{})
		lev := []*TreeNode{}
		for _, node := range queue {
			ans[len(ans)-1] = append(ans[len(ans)-1], node.Val)
			if node.Left != nil {
				lev = append(lev, node.Left)
			}
			if node.Right != nil {
				lev = append(lev, node.Right)
			}
		}
		queue = lev
	}
	return ans
}
