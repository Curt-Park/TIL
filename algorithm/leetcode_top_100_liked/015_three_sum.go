import "sort"

func threeSum(nums []int) [][]int {
	ans, i := [][]int{}, -1
	sort.Ints(nums)
	for i < len(nums)-2 {
		i += 1
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		l, r := i+1, len(nums)-1
		for l < r {
			if nums[l]+nums[r] == -nums[i] {
				ans = append(ans, []int{nums[i], nums[l], nums[r]})
				l, r = l+1, r-1
				for l < len(nums)-1 && nums[l-1] == nums[l] {
					l += 1
				}
				for r > 0 && nums[r+1] == nums[r] {
					r -= 1
				}
			} else if nums[l]+nums[r] < -nums[i] {
				l += 1
			} else {
				r -= 1
			}
		}
	}
	return ans
}
