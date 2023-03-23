func maxArea(height []int) int {
	l, r, ans := 0, len(height)-1, 0
	for l < r {
		w := (r - l) * min(height[l], height[r])
		ans = -min(-ans, -w) // max
		if height[l] < height[r] {
			l += 1
		} else {
			r -= 1
		}
	}
	return ans
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
