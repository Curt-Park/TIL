package main

func combinationSum(candidates []int, target int) [][]int {
	combinations := [][]int{}
	var backtracking func(int, int, []int)
	backtracking = func(idx int, target int, combination []int) {
		if target == 0 {
			cpy := make([]int, len(combination))
			copy(cpy, combination)
			combinations = append(combinations, cpy)
		} else if target > 0 {
			for i := idx; i < len(candidates); i++ {
				nextTarget := target - candidates[i]
				if nextTarget < 0 {
					continue
				}
				backtracking(i, nextTarget, append(combination, candidates[i]))
			}
		}
	}
	backtracking(0, target, []int{})
	return combinations
}
