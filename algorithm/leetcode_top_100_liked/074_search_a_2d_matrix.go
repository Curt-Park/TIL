package main

func searchMatrix(matrix [][]int, target int) bool {
	m, n := len(matrix), len(matrix[0])
	l, r, idx := 0, m*n, -1
	for l < r {
		mid := (l + r) / 2
		midVal := getValue(&matrix, mid)
		if midVal == target {
			idx = mid
			break
		} else if midVal < target {
			l = mid + 1
		} else {
			r = mid
		}
	}
	if idx == -1 {
		return false
	}
	return true
}

func getValue(matrix *[][]int, idx int) int {
	n := len((*matrix)[0])
	r, c := idx/n, idx%n
	return (*matrix)[r][c]
}
