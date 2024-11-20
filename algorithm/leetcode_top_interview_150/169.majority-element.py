#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return max(Counter(nums).items(), key=lambda x: x[1])[0]
# @lc code=end

