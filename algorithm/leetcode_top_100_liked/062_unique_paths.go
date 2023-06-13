package main

func uniquePaths1(m int, n int) int {
	row := make([]int, n)
	for i := 0; i < n; i++ {
		row[i] = 1
	}
	for i := 1; i < m; i++ {
		for j := n - 2; j >= 0; j-- {
			row[j] += row[j+1]
		}
	}
	return row[0]
}

func uniquePaths2(m int, n int) int {
	paths := map[[2]int]int{}
	var find func(int, int) int
	find = func(r, c int) int {
		if r == m || c == n {
			return 0
		}
		if r == m-1 && c == n-1 {
			return 1
		}
		if _, exists := paths[[2]int{r, c}]; exists {
			return paths[[2]int{r, c}]
		}
		paths[[2]int{r, c}] = find(r+1, c) + find(r, c+1)
		return paths[[2]int{r, c}]
	}
	return find(0, 0)
}
