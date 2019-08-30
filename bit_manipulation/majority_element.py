"""
https://leetcode.com/problems/majority-element/

169. Majority Element
Easy


Given an array of size n, find the majority element.
The majority element is the element that appears
more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and
the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

from typing import List


class Solution:
    def majorityElement4(self, nums: List[int]) -> int:
        """O(N) / O(1)"""
        cnt, ret = [0] * 32, 0
        for i in range(32):
            for n in nums:
                cnt[i] += (n >> i) & 1
            ret |= (len(nums) // 2 < cnt[i]) << i
        return ret - (1 << 32) if (ret >> 31) & 1 else ret
    
    # Boyd-Moore voting algorithm
    def majorityElement3(self, nums: List[int]) -> int:
        """O(N), O(1) """
        candi, cnt = None, 0
        for n in nums:
            candi = n if cnt == 0 else candi
            cnt += 1 if n == candi else -1
        return candi
        
    def majorityElement2(self, nums: List[int]) -> int:
        """O(NlogN), O(1)"""
        return sorted(nums)[len(nums) // 2]

    def majorityElement1(self, nums: List[int]) -> int:
        """O(N), O(N)"""
        cnt = {}
        for n in nums:
            cnt[n] = cnt.get(n, 0) + 1
            if len(nums) // 2 < cnt[n]:
                return n
        return None
