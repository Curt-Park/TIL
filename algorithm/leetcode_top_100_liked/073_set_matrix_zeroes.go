package main

func setZeroes(matrix [][]int) {
	rowMap := map[int]bool{}
	colMap := map[int]bool{}
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[0]); j++ {
			if matrix[i][j] == 0 {
				rowMap[i] = true
				colMap[j] = true
			}
		}
	}
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[0]); j++ {
			if _, exist := rowMap[i]; exist {
				matrix[i][j] = 0
			}
			if _, exist := colMap[j]; exist {
				matrix[i][j] = 0
			}
		}
	}
}
