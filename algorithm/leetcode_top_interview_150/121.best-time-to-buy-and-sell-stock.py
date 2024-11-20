#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m, ret = 0, 0
        for n in prices[::-1]:
             m = max(m, n)
             ret = max(ret, m - n)
        return ret
# @lc code=end

