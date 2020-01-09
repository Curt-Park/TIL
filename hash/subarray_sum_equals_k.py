"""
https://leetcode.com/problems/subarray-sum-equals-k/
560. Subarray Sum Equals K
Medium


Given an array of integers and an integer k,
you need to find the total number of continuous subarrays
whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
Note:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and
the range of the integer k is [-1e7, 1e7].
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """ O(N), O(N)"""
        tot, cnt, dic = 0, 0, {0: 1}
        for n in nums:
            tot += n
            if tot - k in dic:
                cnt += dic[tot - k]
            dic[tot] = dic.get(tot, 0) + 1
        return cnt
