"""
https://leetcode.com/problems/merge-intervals/

56. Merge Intervals
Medium

Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """O(NlogN) / O(N)"""
        ret = []
        for interval in sorted(intervals):
            if ret and ret[-1][0] <= interval[0] <= ret[-1][1]:
                ret[-1][1] = max(ret[-1][1], interval[1])
            else:
                ret += interval,
        return ret
