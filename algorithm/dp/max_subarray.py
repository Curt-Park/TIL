"""
https://leetcode.com/problems/maximum-subarray/

53. Maximum Subarray
Easy

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6

Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


class Solution:
    def maxSubArray2(self, nums: List[int]) -> int:
        """O(N) / O(1)"""
        ret = nums[0] if len(nums) else 0
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            ret = max(ret, nums[i])
        return ret

    def maxSubArray1(self, nums: List[int]) -> int:
        """O(N) / O(1)"""
        ret, s = nums[0] if nums else 0, 0
        for n in nums:
            ret = max(ret, s + n)
            s = max(s + n, 0)
        return ret
