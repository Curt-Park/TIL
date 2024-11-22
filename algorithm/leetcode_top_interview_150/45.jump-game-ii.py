#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    # O(N^2)
    def jump_0(self, nums: List[int]) -> int:
        n_jumps, N = [float("inf")] * len(nums), len(nums)
        n_jumps[-1] = 0
        for i in reversed(range(N-1)):
            if not nums[i]:
                continue
            lookup = n_jumps[i+1:i+nums[i]+1]
            n_jumps[i] = min(lookup) + 1
        return n_jumps[0]

    def jump(self, nums: List[int]) -> int:
        pass
# @lc code=end

