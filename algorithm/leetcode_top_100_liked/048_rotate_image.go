package main

func rotate1(matrix [][]int) {
	reverse := func(indices [][]int) {
		for i, j := 0, len(indices)-1; i < j; i, j = i+1, j-1 {
			r1, c1 := indices[i][0], indices[i][1]
			r2, c2 := indices[j][0], indices[j][1]
			matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
		}
	}
	for i := 0; i < len(matrix); i++ {
		indices := [][]int{}
		for j := 0; j < len(matrix); j++ {
			indices = append(indices, []int{i, j})
		}
		reverse(indices)
	}
	starts := [][]int{{0, 0}}
	for i := 1; i < len(matrix); i++ {
		starts = append(starts, []int{0, i})
		starts = append(starts, []int{i, 0})
	}
	for _, start := range starts {
		indices := [][]int{}
		r, c := start[0], start[1]
		for r < len(matrix) && c < len(matrix) {
			indices = append(indices, []int{r, c})
			r, c = r+1, c+1
		}
		reverse(indices)
	}
}

func rotate2(matrix [][]int) {
	for i := 0; i < len(matrix); i++ {
		for j := i; j < len(matrix); j++ {
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		}
	}
	for i := 0; i < len(matrix); i++ {
		for l, r := 0, len(matrix)-1; l < r; l, r = l+1, r-1 {
			matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
		}
	}
}

func rotate3(matrix [][]int) {
	for i := 0; i < len(matrix); i++ {
		for j := i; j < len(matrix); j++ {
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		}
		for l, r := 0, len(matrix)-1; l < r; l, r = l+1, r-1 {
			matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
		}
	}
}
