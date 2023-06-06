package main

func trap1(height []int) int {
	sum := 0
	for i := 1; i < len(height); i++ {
		l, r := height[i], height[i]
		for j := i - 1; j >= 0; j-- {
			if height[j] > l {
				l = height[j]
			}
		}
		for k := i + 1; k < len(height); k++ {
			if height[k] > r {
				r = height[k]
			}
		}
		var h int
		if l < r {
			h = l
		} else {
			h = r
		}
		sum += (h - height[i])
		height[i] = h
	}
	return sum
}

func trap2(height []int) int {
	sum := 0
	lMax := make([]int, len(height))
	rMax := make([]int, len(height))
	lMax[0], rMax[len(height)-1] = height[0], height[len(height)-1]

	for i := 1; i < len(height); i++ {
		if height[i] > lMax[i-1] {
			lMax[i] = height[i]
		} else {
			lMax[i] = lMax[i-1]
		}
	}
	for i := len(height) - 2; i >= 0; i-- {
		if height[i] > rMax[i+1] {
			rMax[i] = height[i]
		} else {
			rMax[i] = rMax[i+1]
		}
	}
	for i := 0; i < len(height); i++ {
		if rMax[i] > lMax[i] {
			sum += lMax[i]
		} else {
			sum += rMax[i]
		}
		sum -= height[i]
	}
	return sum
}

func trap3(height []int) int {
	sum, l, r := 0, 0, len(height)-1
	lMax, rMax := 0, 0
	for l < r {
		if height[l] < height[r] {
			if lMax < height[l] {
				lMax = height[l]
			}
			sum += lMax - height[l]
			l += 1

		} else {
			if rMax < height[r] {
				rMax = height[r]
			}
			sum += rMax - height[r]
			r -= 1
		}
	}
	return sum
}
