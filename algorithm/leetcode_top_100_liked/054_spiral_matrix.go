package main

func spiralOrder(matrix [][]int) []int {
	m, n := len(matrix), len(matrix[0])
	right, left, up, down := [2]int{0, 1}, [2]int{0, -1}, [2]int{-1, 0}, [2]int{1, 0}
	current, direction := [2]int{0, 0}, right
	ans := []int{}
	for len(ans) < m*n {
		ans = append(ans, matrix[current[0]][current[1]])
		matrix[current[0]][current[1]] = -101 // visited

		next := [2]int{current[0] + direction[0], current[1] + direction[1]}
		if next[0] < 0 || next[0] >= m ||
			next[1] < 0 || next[1] >= n ||
			matrix[next[0]][next[1]] == -101 {
			if direction == right {
				direction = down
			} else if direction == down {
				direction = left
			} else if direction == left {
				direction = up
			} else if direction == up {
				direction = right
			}
		}
		current[0] = current[0] + direction[0]
		current[1] = current[1] + direction[1]
	}
	return ans
}
