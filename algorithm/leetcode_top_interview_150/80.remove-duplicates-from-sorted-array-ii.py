#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#
# @lc code=start

from collections import Counter

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ret = 0
        for n, c in sorted(Counter(nums).items()):
            nums[ret] = nums[ret + (c >= 2)] = n
            ret += min(2, c)
        return ret
# @lc code=end