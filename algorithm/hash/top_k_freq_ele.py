"""
https://leetcode.com/problems/top-k-frequent-elements/

347. Top K Frequent Elements
Medium

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

import heapq
from collections import Counter
from itertools import chain


class Solution:
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        """Bucket sort: O(N) / O(N)"""
        freqmap = [[] for _ in nums]
        for n, cnt in Counter(nums).items():
            freqmap[-cnt].append(n)
        return list(chain.from_iterable(freqmap))[:k]

    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        """Heap: O(NlogK) / O(N)"""
        pq = []
        for n, cnt in Counter(nums).items():
            heapq.heappush(pq, (cnt, n))
            if k < len(pq):
                heapq.heappop(pq)
        return [n for _, n in pq]
