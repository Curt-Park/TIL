"""
https://leetcode.com/problems/non-overlapping-intervals

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.



Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


Note:
You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
"""

class Solution:
    def eraseOverlapIntervalsGreedy(self, intervals: List[List[int]]) -> int:
        """O(NlogN), O(N)"""
        end, cnt = float("-inf"), 0
        for interval in sorted(intervals, key=lambda interval: interval[1]):
            if end > interval[0]:
                cnt += 1
            else:
                end = interval[1]
        return cnt

    def eraseOverlapIntervalsSorted(self, intervals: List[List[int]]) -> int:
        """O(NlogN), O(N)"""
        tmp, cnt = None, 0
        for interval in sorted(intervals):
            if tmp and tmp[0] <= interval[0] < tmp[1]:
                tmp[1], cnt = min(tmp[1], interval[1]), cnt + 1
            else:
                tmp = interval
        return cnt
