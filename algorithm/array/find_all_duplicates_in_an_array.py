"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/

442. Find All Duplicates in an Array
Medium

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""


from collections import Counter


class Solution:
    def findDuplicatesSwap(self, nums: List[int]) -> List[int]:
        """O(N) / O(1)"""
        i, nums_twice = 0, []
        while i < len(nums):
            if nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1
        for i, n in enumerate(nums):
            if n != i + 1:
                nums_twice.append(n)
        return nums_twice

    def findDuplicatesHash(self, nums: List[int]) -> List[int]:
        """O(N) / O(1)"""
        nums_twice = []
        for n in nums:
            if nums[abs(n) - 1] < 0:
                nums_twice.append(abs(n))
            nums[abs(n) - 1] *= -1
        return nums_twice

    def findDuplicatesN(self, nums: List[int]) -> List[int]:
        """O(N) / O(N)"""
        return [n for n, cnt in Counter(nums).items() if cnt == 2]
