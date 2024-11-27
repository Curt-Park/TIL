#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
class Solution:
    # O(C x N) / O(1)
    def hIndex_0(self, citations: List[int]) -> int:
        m = max(citations)
        for i in range(m, -1, -1):
            n = sum(c >= i for c in citations)
            if i <= n:
                return i
        return 0

    # O(min(C, N) x N) / O(1)
    def hIndex_1(self, citations: List[int]) -> int:
        m = min(max(citations), len(citations))
        for i in range(m, -1, -1):
            n = sum(c >= i for c in citations)
            if i <= n:
                return i
        return 0

    # O(NlogN) / O(N)
    def hIndex_2(self, citations: List[int]) -> int:
        hist = [0] * (len(citations) + 1)
        for c in reversed(sorted(citations)):
            if c > len(citations):
                hist[len(citations)] += 1
            else:
                hist[c] += 1
        for i in range(len(citations), -1, -1):
            if i < len(citations):
                hist[i] += hist[i + 1]
            if i <= hist[i]:
                return i
        return 0

    # O(N) / O(N)
    def hIndex(self, citations: List[int]) -> int:
        hist, cnt = [0] * (len(citations) + 1), 0
        for c in citations:
            if c > len(citations):
                hist[len(citations)] += 1
            else:
                hist[c] += 1
        for i in range(len(citations), -1, -1):
            cnt += hist[i]
            if i <= cnt:
                return i
        return 0

# @lc code=end

