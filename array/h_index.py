"""
https://leetcode.com/problems/h-index/

274. H-Index
Medium

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3

Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had
             received 3, 0, 6, 1, 5 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.
"""


class Solution:
    def hIndexHist(self, citations: List[int]) -> int:
        """O(N) / O(N)"""
        hist, cnt = [0] * (len(citations) + 1), 0
        for n in citations:
            if n >= len(hist): hist[-1] += 1
            else: hist[n] += 1
        for i in range(len(citations), -1, -1):
            cnt += hist[i]
            if cnt >= i: return i
        return 0

    def hIndexSort(self, citations: List[int]) -> int:
        """O(NlogN) / O(1)"""
        citations.sort()
        for h in range(len(citations), 0, -1):
            if h <= citations[len(citations) - h]:
                return h
        return 0

    def hIndexSlow(self, citations: List[int]) -> int:
        """O(N^2) / O(1)"""
        for h in range(len(citations), -1, -1):
            eq_h = at_least_h = 0
            for n in citations:
                eq_h += 1 if h == n else 0
                at_least_h += 1 if h <= n else 0
            if at_least_h - eq_h <= h <= at_least_h:
                return h
        return 0
