package main

func maxProduct(nums []int) int {
	minVal, maxVal, ans := 1, 1, nums[0]
	for _, val := range nums {
		nextMinVal := min(val, min(minVal*val, maxVal*val))
		nextMaxVal := max(val, max(minVal*val, maxVal*val))
		minVal, maxVal = nextMinVal, nextMaxVal
		ans = max(ans, maxVal)
	}
	return ans
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	return -min(-a, -b)
}
