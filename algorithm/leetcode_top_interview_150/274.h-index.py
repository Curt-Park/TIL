#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
class Solution:
    # O(1000 x N) / O(1)
    def hIndex(self, citations: List[int]) -> int:
        m = max(citations)
        for i in range(m, -1, -1):
            n = sum(c >= i for c in citations)
            if i <= n:
                return i
        return 0
        
# @lc code=end

