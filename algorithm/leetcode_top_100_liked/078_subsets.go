package main

func subsets(nums []int) [][]int {
	upper, ans := 1, [][]int{}
	for i := 0; i < len(nums); i++ {
		upper = upper << 1
	}
	for i := 0; i < upper; i++ {
		ck, arr := i, []int{}
		for j := 0; j < len(nums); j++ {
			if 1&(ck>>j) > 0 {
				arr = append(arr, nums[len(nums)-j-1])
			}
		}
		ans = append(ans, arr)
	}
	return ans
}
