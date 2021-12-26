"""
https://leetcode.com/problems/move-zeroes/

283. Move Zeroes
Easy

Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution:
    def moveZeroes3(self, nums: List[int]) -> None:
        """O(N) / O(1)
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
            if not nums[i]: continue
            nums[pos], nums[i], pos = nums[i], nums[pos], pos + 1

    def moveZeroes2(self, nums: List[int]) -> None:
        """O(NlogN) / O(1)
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=lambda x: 0 if x else 1)

    def moveZeroes1(self, nums: List[int]) -> None:
        """O(N^2) / O(1)
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            while i > 0 and nums[i] and nums[i-1] == 0:
                nums[i-1], nums[i], i = nums[i], nums[i-1], i - 1
