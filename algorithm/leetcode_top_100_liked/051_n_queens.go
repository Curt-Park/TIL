package main

import "strings"

func solveNQueens2(n int) [][]string {
	ans := [][]string{}
	queens := map[int]int{}
	find(0, n, &queens, &ans)
	return ans
}

func find(row int, n int, queens *map[int]int, ans *[][]string) {
	if row == n {
		place := []string{}
		for i := 0; i < n; i++ {
			row := strings.Repeat(".", (*queens)[i]) + "Q"
			row += strings.Repeat(".", n-(*queens)[i]-1)
			place = append(place, row)
		}
		*ans = append(*ans, place)
	}
	for col := 0; col < n; col++ {
		isValid := true
		for r, c := range *queens {
			if c == col || row-r == col-c || row-r == c-col {
				isValid = false
				break
			}
		}
		if isValid {
			(*queens)[row] = col
			find(row+1, n, queens, ans)
			delete(*queens, row)
		}
	}
}

func solveNQueens1(n int) [][]string {
	ans := [][]string{}
	board := [][]int{}
	for i := 0; i < n; i++ {
		board = append(board, make([]int, n))
	}
	find := func(int, []string) {}
	find = func(row int, place []string) {
		if row == n {
			cpy := make([]string, len(place))
			copy(cpy, place)
			ans = append(ans, cpy)
			return
		}
		for i := 0; i < n; i++ {
			if board[row][i] != 0 {
				continue
			}
			place[row] = place[row][:i] + "Q" + place[row][i+1:]
			for j := row + 1; j < n; j++ {
				offset := j - row
				if i-offset >= 0 {
					board[j][i-offset] += 1
				}
				board[j][i] += 1
				if i+offset < n {
					board[j][i+offset] += 1
				}
			}
			find(row+1, place)
			for j := row + 1; j < n; j++ {
				offset := j - row
				if i-offset >= 0 {
					board[j][i-offset] -= 1
				}
				board[j][i] -= 1
				if i+offset < n {
					board[j][i+offset] -= 1
				}
			}
			place[row] = place[row][:i] + "." + place[row][i+1:]
		}
	}
	// init
	place := []string{}
	for i := 0; i < n; i++ {
		row := []string{}
		for j := 0; j < n; j++ {
			row = append(row, ".")
		}
		place = append(place, strings.Join(row, ""))
	}
	// run
	find(0, place)
	return ans
}
