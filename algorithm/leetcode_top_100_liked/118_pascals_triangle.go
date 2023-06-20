package main

func generate(numRows int) [][]int {
	ans := [][]int{}
	ans = append(ans, []int{1})
	for i := 1; i < numRows; i++ {
		row := []int{}
		row = append(row, 1)
		for j := 1; j < len(ans[len(ans)-1]); j++ {
			row = append(row, ans[len(ans)-1][j-1]+ans[len(ans)-1][j])
		}
		row = append(row, 1)
		ans = append(ans, row)
	}
	return ans
}
