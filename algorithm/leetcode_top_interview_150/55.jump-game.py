#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump_0(self, nums: List[int]) -> bool:
        possible = [False] * len(nums)
        possible[-1] = True
        for i in range(len(nums) - 2, -1, -1):
            if any(possible[i:i+nums[i]+1]):
                possible[i] = True
        return possible[0]

    def canJump(self, nums: List[int]) -> bool:
        reachable, n = 0, len(nums)
        for i in range(n - 2, -1, -1):
            if (n - 1) - i <= nums[i] + reachable:
                reachable = n - 1 - i
        return reachable == n - 1
# @lc code=end

