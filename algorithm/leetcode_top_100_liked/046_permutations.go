package main

func permute(nums []int) [][]int {
	ans := [][]int{}
	var find func(int, []int)
	find = func(idx int, arr []int) {
		if idx == len(arr) {
			cpy := make([]int, len(arr))
			copy(cpy, arr)
			ans = append(ans, cpy)
		}
		for i := idx; i < len(arr); i++ {
			nums[idx], nums[i] = nums[i], nums[idx]
			arr[idx] = nums[idx]
			find(idx+1, arr)
			nums[idx], nums[i] = nums[i], nums[idx]
		}
	}
	find(0, make([]int, len(nums)))
	return ans
}
