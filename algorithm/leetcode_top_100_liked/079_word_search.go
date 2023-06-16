package main

func exist(board [][]byte, word string) bool {
	visited := map[[2]int]bool{}
	var search func(int, int, int) bool
	search = func(r, c, i int) bool {
		if i == len(word) {
			return true
		}
		if r < 0 || r >= len(board) ||
			c < 0 || c >= len(board[0]) {
			return false
		}
		if board[r][c] != word[i] {
			return false
		}
		if _, exist := visited[[2]int{r, c}]; exist {
			return false
		}
		visited[[2]int{r, c}] = true
		up := search(r-1, c, i+1)
		down := search(r+1, c, i+1)
		left := search(r, c-1, i+1)
		right := search(r, c+1, i+1)
		delete(visited, [2]int{r, c})
		return up || down || left || right
	}
	for r := 0; r < len(board); r++ {
		for c := 0; c < len(board[0]); c++ {
			if search(r, c, 0) {
				return true
			}
		}
	}
	return false
}
