package main

func maxSubArray(nums []int) int {
	sum := 0
	max := -10000
	for i := 0; i < len(nums); i++ {
		sum += nums[i]
		if sum > max {
			max = sum
		}
		if sum < 0 {
			sum = 0
		}
	}
	return max
}
