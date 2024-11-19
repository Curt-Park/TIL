#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#
from collections import Counter

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = []
        for n in nums:
            if not cnt or cnt[-1][0] != n:
                cnt.append([n, 1])
            else:
                cnt[-1][1] += 1

        l = 0
        for n, c in cnt:
            for i in range(min(c, 2)):
                nums[l+i] = n
            l += min(c, 2)

        return l
# @lc code=end

