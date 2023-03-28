import "math"

func search(nums []int, target int) int {
	l, r, num := 0, len(nums)-1, 0
	for l <= r {
		mid := (l + r) / 2
		if (nums[0] > nums[mid]) == (nums[0] > target) {
			num = nums[mid]
		} else if nums[0] > nums[mid] {
			num = math.MaxInt
		} else {
			num = math.MinInt
		}
		if target < num {
			r = mid - 1
		} else if target > num {
			l = mid + 1
		} else {
			return mid
		}
	}
	return -1
}
