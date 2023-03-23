package main

import (
	"fmt"
	"math"
)

// O(N)
func findMedianSortedArrays1(nums1 []int, nums2 []int) float64 {
	var m []int
	p1, p2 := 0, 0
	for p1 < len(nums1) && p2 < len(nums2) {
		if nums1[p1] < nums2[p2] {
			m = append(m, nums1[p1])
			p1 += 1
		} else {
			m = append(m, nums2[p2])
			p2 += 1
		}
	}
	for p1 < len(nums1) {
		m = append(m, nums1[p1])
		p1 += 1
	}
	for p2 < len(nums2) {
		m = append(m, nums2[p2])
		p2 += 1
	}

	if (len(nums1)+len(nums2))%2 == 1 {
		return float64(m[len(m)/2])
	}
	return float64(m[len(m)/2]+m[len(m)/2-1]) / 2.0
}

/*
Case 01: [1, 2, 3, 4], [5, 6, 7]
Step1: 1 2 / 3 4, 5 / 6 7
=> 2 < 6, 3 < 5!
Step2: 1 2 3 / 4, / 5 6 7
=> 3 < 5, -inf < 4
=> max(3, -inf), min(4, 5)
=> 4

Case 02: [1, 3, 5, 7], [2, 4, 6]
Step1: 1 3 / 5 7, 2 / 4 6
=> 3 < 4, 5 > 2
=> max(3, 2), min(4, 5)
=> 4

Case 03: [1, 2, 3, 4, 5], [0]
Step1: 1 2 / 3 4 5, 0 /
=> 2 < inf, 3 > 0
=> max(2, 0), min(3, inf)
=> 2, 3

Case 04: [1, 3], [2]
Step1: 1 / 3, 2 /
=> max(1, 2), min(3, inf)
=> 2

Case 05: [1, 2], [3, 4]
Step1: 1 / 2, 3 / 4
=> 1 < 4, 2 < 3!
Step2: 1 2 /, / 3, 4
=> 2 < 3, inf > -inf
=> max(2, -inf), min(inf, 3)
=> 2, 3

Case 06: [3, 4, 5, 6], [0, 1, 2]
Step1: 3 4 / 5 6, 0 / 1 2
=> 4 > 1!, 5 > 0
Step2: 3 / 4 5 6, 0 1 / 2
=> 3 > 2!, 4 > 1
Step3: / 3 4 5 6, 0 1 2 /
=> -inf < inf, 3 > 2
=> max(-inf, 2), min(3, inf)
=> 3
*/
// O(logN)
func findMedianSortedArrays2(nums1 []int, nums2 []int) float64 {
	len1, len2 := len(nums1), len(nums2)
	if len1 > len2 { // nums2 is always longer than nums1.
		return findMedianSortedArrays2(nums2, nums1)
	}

	k := (len1 + len2 - 1) / 2
	l, r := 0, len1 // the shorter array's pointers.
	for l < r {
		mid1 := (l + r) / 2
		mid2 := k - mid1

		// check it is the right partitions.
		if nums1[mid1] < nums2[mid2] {
			l = mid1 + 1
		} else {
			r = mid1
		}
	}

	// get the numbers alongside mid1.
	l1, l2, r1, r2 := math.MinInt64, math.MinInt64, math.MaxInt64, math.MaxInt64
	if l > 0 {
		l1 = nums1[l-1]
	}
	if l < len1 {
		r1 = nums1[l]
	}

	// get the numbers alongside mid2.
	if k-l >= 0 {
		l2 = nums2[k-l]
	}
	if k-l+1 < len2 {
		r2 = nums2[k-l+1]
	}

	a, b := math.Max(float64(l1), float64(l2)), math.Min(float64(r1), float64(r2))
	if (len1+len2)%2 == 1 {
		return 2 * a / 2.
	}
	return (a + b) / 2.
}

func main() {
	fmt.Println(findMedianSortedArrays2([]int{1, 2, 3, 4}, []int{5, 6, 7}))
	fmt.Println(findMedianSortedArrays2([]int{1, 3, 5, 7}, []int{2, 4, 6}))
	fmt.Println(findMedianSortedArrays2([]int{1, 2, 3, 4, 5}, []int{0}))
	fmt.Println(findMedianSortedArrays2([]int{1, 3}, []int{2}))
	fmt.Println(findMedianSortedArrays2([]int{1, 2}, []int{3, 4}))
	fmt.Println(findMedianSortedArrays2([]int{3, 4, 5, 6}, []int{0, 1, 2}))
}
