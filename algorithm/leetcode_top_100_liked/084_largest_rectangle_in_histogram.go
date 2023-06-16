package main

// TLE
func largestRectangleArea(heights []int) int {
	ans := 0
	for i, h := range heights {
		l, r := i, i
		for l > 0 && heights[l-1] >= h {
			l -= 1
		}
		for r < len(heights)-1 && heights[r+1] >= h {
			r += 1
		}
		if ans < h*(r-l+1) {
			ans = h * (r - l + 1)
		}
	}
	return ans
}
