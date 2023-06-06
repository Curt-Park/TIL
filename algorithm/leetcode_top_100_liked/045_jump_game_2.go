package main

import "math"

func jump1(nums []int) int {
	m := make([]int, len(nums))
	for i := 1; i < len(nums); i++ {
		m[i] = int(math.Pow(10, 7))
	}
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j <= i+nums[i] && j < len(nums); j++ {
			if m[j] > m[i]+1 {
				m[j] = m[i] + 1
			}
		}
	}
	return m[len(nums)-1]
}

func jump2(nums []int) int {
	m := make([]int, len(nums))
	seen := 0
	for i := 1; i < len(nums); i++ {
		m[i] = int(math.Pow(10, 7))
	}
	for i := 0; i < len(nums); i++ {
		for j := seen + 1; j <= i+nums[i] && j < len(nums); j++ {
			if m[j] > m[i]+1 {
				m[j] = m[i] + 1
			}
			seen = j
		}
	}
	return m[len(nums)-1]
}

func jump3(nums []int) int {
	far, end, cnt := 0, 0, 0
	for i := 0; i < len(nums)-1; i++ {
		if i+nums[i] > far {
			far = i + nums[i]
		}
		if i == end {
			cnt += 1
			end = far
		}
	}
	return cnt
}
