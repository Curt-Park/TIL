"""
https://leetcode.com/problems/first-missing-positive/

41. First Missing Positive
Hard

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3

Example 2:

Input: [3,4,-1,1]
Output: 2

Example 3:

Input: [7,8,9,11,12]
Output: 1

Note:
Your algorithm should run in O(n) time and uses constant extra space.

[1, 2, 0]
[1, 2, -1]
=> 3

[3, 4, -1, 1]
[-1, 4, 3, 1]
[-1, 1, 3, 4]
[1, -1, 3, 4]
=> 2

[7, 8, 9, 11, 12]
[-1, -1, -1, -1, -1]
=> 1

[4, 0, 2, 3]
[3, 0, 2, 4]
[2, 0, 3, 4]
[0, 2, 3, 4]
[-1, 2, 3, 4]
=> 1
"""

from typing import List


class Solution:
    def firstmissingpositive2(self, nums: list[int]) -> int:
        """O(N) / O(1)"""
        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

    def firstMissingPositive1(self, nums: List[int]) -> int:
        """O(N) / O(N)"""
        return min(set(range(1, len(nums) + 2)) - set(nums))
