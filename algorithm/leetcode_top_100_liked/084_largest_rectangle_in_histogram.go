package main

func largestRectangleArea1(heights []int) int {
	area := make([]int, len(heights))
	getArea(&heights, &area)
	for i := 0; i < len(heights)/2; i++ {
		heights[i], heights[len(heights)-i-1] = heights[len(heights)-i-1], heights[i]
		area[i], area[len(heights)-i-1] = area[len(heights)-i-1], area[i]
	}
	getArea(&heights, &area)
	maxArea := 0
	for i := 0; i < len(heights); i++ {
		area := area[i] - heights[i]
		if maxArea < area {
			maxArea = area
		}
	}
	return maxArea
}

func getArea(heights *[]int, area *[]int) {
	stack := []int{}
	for i, h := range *heights {
		if len(stack) > 0 {
			loc := stack[len(stack)-1]
			for len(stack) > 0 && (*heights)[stack[len(stack)-1]] > h {
				idx := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				(*area)[idx] += (*heights)[idx] * (loc - idx + 1)
			}
		}
		stack = append(stack, i)
	}
	if len(stack) > 0 {
		loc := stack[len(stack)-1]
		for len(stack) > 0 {
			idx := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			(*area)[idx] += (*heights)[idx] * (loc - idx + 1)
		}
	}
}

// TLE
func largestRectangleArea2(heights []int) int {
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
