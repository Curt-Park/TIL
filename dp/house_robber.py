"""
https://leetcode.com/problems/house-robber/

198. House Robber
Easy

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        """O(N) / O(1)"""
        dp = [0] + nums[:2]
        for i in range(2, len(nums)):
            dp[0], dp[1], dp[2] = dp[1], dp[2], nums[i]
            dp[2] += max(dp[0], dp[1] - nums[i-1])
        return max(dp)
        
    def rob(self, nums: List[int]) -> int:
        """O(N) / O(N)"""
        dp = nums[:]
        for i in range(2, len(dp)):
            dp[i] += max(dp[i-2], dp[i-1] - nums[i-1])
        return max(dp[-2:] + [0])
