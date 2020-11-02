"""
https://leetcode.com/problems/third-maximum-number/

414. Third Maximum Number
Easy

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""


import heapq


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """O(N) / O(N)"""
        nums, pq = set(nums), []
        for n in nums:
            heapq.heappush(pq, n)
            if len(pq) > 3:
                heapq.heappop(pq)
        return len(nums) < 3 and max(nums) or heapq.heappop(pq)
