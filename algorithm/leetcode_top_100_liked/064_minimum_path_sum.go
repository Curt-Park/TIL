package main

func minPathSum(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	dp := make([]int, n)
	dp[n-1] = grid[m-1][n-1]
	for i := n - 2; i >= 0; i-- {
		dp[i] = grid[m-1][i] + dp[i+1]
	}

	for i := m - 2; i >= 0; i-- {
		dp[n-1] += grid[i][n-1]
		for j := n - 2; j >= 0; j-- {
			dp[j] = grid[i][j] + min(dp[j], dp[j+1])
		}
	}
	return dp[0]
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
