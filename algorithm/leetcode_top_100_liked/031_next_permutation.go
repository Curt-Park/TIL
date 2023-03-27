func nextPermutation(nums []int) {
	asc := -1
	for i := len(nums) - 1; i > 0; i-- {
		if nums[i-1] < nums[i] {
			asc = i - 1
			break
		}
	}
	if asc == -1 {
		reverse(nums)
		return
	}
	for i := len(nums) - 1; i > asc; i-- {
		if nums[asc] < nums[i] {
			nums[asc], nums[i] = nums[i], nums[asc]
			break
		}
	}
	reverse(nums[asc+1:])
}

func reverse(nums []int) {
	for i := 0; i < len(nums)/2; i++ {
		nums[i], nums[len(nums)-i-1] = nums[len(nums)-i-1], nums[i]
	}
}
