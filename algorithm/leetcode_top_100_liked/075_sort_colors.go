package main

import "sort"

func sortColors3(nums []int) {
	pnt0, pnt1, pnt2 := 0, 0, len(nums)-1
	for pnt1 <= pnt2 {
		if nums[pnt1] == 0 {
			nums[pnt0], nums[pnt1] = nums[pnt1], nums[pnt0]
			pnt0, pnt1 = pnt0+1, pnt1+1
		} else if nums[pnt1] == 2 {
			nums[pnt2], nums[pnt1] = nums[pnt1], nums[pnt2]
			pnt2 = pnt2 - 1
		} else {
			pnt1 += 1
		}
	}
}

func sortColors2(nums []int) {
	cnt0, cnt1, cnt2 := 0, 0, 0
	for _, n := range nums {
		switch n {
		case 0:
			cnt0 += 1
		case 1:
			cnt1 += 1
		case 2:
			cnt2 += 1
		}
	}
	for i := 0; i < len(nums); i++ {
		if cnt0 > 0 {
			nums[i] = 0
			cnt0 -= 1
		} else if cnt1 > 0 {
			nums[i] = 1
			cnt1 -= 1
		} else if cnt2 > 0 {
			nums[i] = 2
			cnt2 -= 1
		}
	}
}

func sortColors1(nums []int) {
	sort.Ints(nums)
}
