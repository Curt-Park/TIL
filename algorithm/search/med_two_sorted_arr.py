"""
https://leetcode.com/problems/median-of-two-sorted-arrays/

4. Median of Two Sorted Arrays
Hard

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5


num1 = [1,2,3,4,5,6,7]
num2 = [8,9,10,11,12,13,14]
len = 14
mid = 6
sol = 7, 8

median
mid2 = (m + n + 1) // 2 - mid1
1. 3, 4 => l: {1,2,3,8,9,10,11}, r: {4,5,6,7,12,13,14} => max(3,11) < min(4,12)? False
2. 5, 2 => l: {1,2,3,4,5, 8, 9}, r: {6,7,10,11,12,13,14} => max(5,9)< min(6,10)? False
3. 6, 1 => l: {1,2,3,4,5,6,8}, r: {7,9,10,11,12,13,14} => max(6,8) < min(7,9)? False
3. 7, 0 => l: {1,2,3,4,5,6,7}, r: {8,9,10,11,12,13,14} => max(7, -inf) < min(inf,  8)? True
mid = 7, 8

num1 = [4,5,6,7]
num2 = [1,2,3,8]
len = 8
mid = 4, 5

median
1. 2, 2 => l: {4,5,1,2}, r: {6,7,3,8} => max(5,2) < min(6,3)? False
2. 1, 3 => l: {1,2,3,4}, r: {5,6,7,8} => max(3,4) < min(5,8)? True
mid = 4, 5

num1 = [2]
num2 = [1, 3]
len = 3

median
1. 0, 1 => l: {1}, r: {2,3} => max(-inf, 1) < min(2,3)? True
mid = 2

num1 = []
num2 = [1,2,3]
len = 3

median
1. 0, 1 => l: {1}, r: {2,3} => max(-inf, 1) < min(inf, 2)? True
"""

from typing import List


class Solution:
    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        """O(log(min(m, n))) / O(1)"""
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        l, r, k = 0, m, (n + m - 1) // 2
        while l < r:
            mid1 = (l + r) // 2
            mid2 = k - mid1
            if nums1[mid1] < nums2[mid2]:
                l = mid1 + 1
            else:
                r = mid1

        lb1 = nums1[l - 1] if l > 0 else float("-inf")
        lb2 = nums2[k - l] if k - l >= 0 else float("-inf")
        rb1 = nums1[l] if l < m else float("inf")
        rb2 = nums2[k - l + 1] if k - l + 1 < n else float("inf")
        a, b = max(lb1, lb2), min(rb1, rb2)
        return [a + b, 2 * a][(m + n) % 2] / 2

    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        """O(m+n) / O(1)"""
        m, n, p1, p2, res = len(nums1), len(nums2), 0, 0, 0
        med1, med2 = (m + n - 1) // 2, (m + n) // 2
        for i in range(med2 + 1):
            if n == p2 or p1 < m and nums1[p1] < nums2[p2]:
                idx, nums, p1 = p1, nums1, p1 + 1
            elif m == p1 or p2 < n and nums2[p2] <= nums1[p1]:
                idx, nums, p2 = p2, nums2, p2 + 1
            if i == med1: res += nums[idx]
            if i == med2: res += nums[idx]
        return res / 2


if __name__ == "__main__":
    import doctest
    doctest.testmod()
