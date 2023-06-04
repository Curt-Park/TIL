package main

func searchRange1(nums []int, target int) []int {
	n := len(nums)
	binarySearch := func(target int) int {
		l, r := 0, n
		for l < r {
			mid := (l + r) / 2
			if nums[mid] < target {
				l = mid + 1
			} else {
				r = mid
			}
		}
		return l
	}
	start := binarySearch(target)
	if n == 0 || start == n || nums[start] != target {
		return []int{-1, -1}
	}
	return []int{start, binarySearch(target+1) - 1}
}

func searchRange0(nums []int, target int) []int {
	start, end, n := -1, -1, len(nums)
	l, r, mid := 0, n, n/2
	for l < r {
		if nums[mid] < target {
			l = mid + 1
		} else if nums[mid] > target {
			r = mid
		} else {
			if mid == 0 || nums[mid-1] < nums[mid] {
				start = mid
				break
			} else {
				r = mid
			}
		}
		mid = (l + r) / 2
	}

	l, r, mid = 0, n, n/2
	for l < r {
		if nums[mid] < target {
			l = mid + 1
		} else if nums[mid] > target {
			r = mid
		} else {
			if mid == n-1 || nums[mid] < nums[mid+1] {
				end = mid
				break
			} else {
				l = mid + 1
			}
		}
		mid = (l + r) / 2
	}
	return []int{start, end}
}
