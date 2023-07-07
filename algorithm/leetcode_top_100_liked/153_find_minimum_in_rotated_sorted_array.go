package main

func findMin(nums []int) int {
	if nums[0] <= nums[len(nums)-1] {
		return nums[0]
	}
	mid := len(nums) / 2
	return min(findMin(nums[:mid]), findMin(nums[mid:]))
}
