"""
https://leetcode.com/problems/sliding-window-maximum/
239. Sliding Window Maximum
Hard

Given an array nums, there is a sliding window of size k which is
moving from the very left of the array to the very right.
You can only see the k numbers in the window.
Each time the sliding window moves right by one position.
Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size
for non-empty array.

Follow up:
Could you solve it in linear time?
"""

import heapq
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        """O(N), O(K)"""
        dq, ret = deque(), []
        for i in range(len(nums)):
            while dq and nums[dq[-1]] < nums[i]: dq.pop()
            dq.append(i)
            if dq[0] <= i - k: dq.popleft()
            if k - 1 <= i: ret.append(nums[dq[0]])
        return ret

    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        """O(NlogN), O(N)"""
        heap, ret = [], []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i < k - 1: continue
            while heap[0][1] <= i - k: heapq.heappop(heap)
            ret.append(-heap[0][0])
        return ret
