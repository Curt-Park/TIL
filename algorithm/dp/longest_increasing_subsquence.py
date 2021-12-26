"""
https://leetcode.com/problems/longest-increasing-subsequence/

300. Longest Increasing Subsequence
Medium

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

Input:      [10,9,2,5,3,7,101,18]
DP:         [10                 ]: 1
            [ 9                 ]: 1
            [ 2                 ]: 1
            [ 2,5               ]: 2
            [ 2,3               ]: 2
            [ 2,3,7             ]: 3
            [ 2,3,7,101         ]: 4
            [ 2,3,7, 18         ]: 4
"""

from bisect import bisect_left


class Solution:
    def lengthOfLIS3(self, nums: List[int]) -> int:
        """O(NlogN) / O(N)"""
        dp = [float("inf")] * len(nums)
        for n in nums:
            dp[bisect_left(dp, n)] = n
        return bisect_left(dp, float("inf"))

    def lengthOfLIS2(self, nums: List[int]) -> int:
        """O(NlogN) / O(N)"""
        dp = []
        for n in nums:
            idx = bisect_left(dp, n)
            if len(dp) == idx:
                dp.append(n)
            else:
                dp[idx] = n
        return len(dp)

    def lengthOfLIS1(self, nums: List[int]) -> int:
        """O(N^2) / O(N)"""
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            dp[i] += max([dp[j] for j in range(i) if nums[j] < nums[i]] or [0])
        return len(nums) and max(dp)
