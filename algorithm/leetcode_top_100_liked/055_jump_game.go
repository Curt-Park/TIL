package main

func canJump1(nums []int) bool {
	lastPossible := len(nums) - 1
	for i := len(nums) - 2; i >= 0; i-- {
		if i+nums[i] >= lastPossible {
			lastPossible = i
		}
	}
	return lastPossible == 0
}

func canJump2(nums []int) bool {
	possible := make([]bool, len(nums))
	possible[len(nums)-1] = true
	for i := len(nums) - 2; i >= 0; i-- {
		for j := i; j <= i+nums[i] && j < len(nums); j++ {
			if possible[j] == true {
				possible[i] = true
				break
			}
		}
	}
	return possible[0]
}
