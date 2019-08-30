"""
https://leetcode.com/problems/missing-number/

268. Missing Number
Easy

Given an array containing n distinct numbers taken from
0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2

Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant extra space complexity?
"""

from functools import reduce
from typing import List


class Solution:
    def missingNumber2(self, nums: List[int]) -> int:
        """O(N) / O(1)"""
        return reduce(lambda x, y: x ^ y, nums + [*range(len(nums)+1)])

    def missingNumber1(self, nums: List[int]) -> int:
        """O(N) / O(1)"""
        bitmask, ret = [0] * 32, 0
        for i in range(32):
            for n, m in enumerate(nums, 1):
                bitmask[i] += ((m >> i) & 1) - ((n >> i) & 1)
            if bitmask[i] < 0:
                ret |= 1 << i
        return ret - (1 << 32) if ret >> 31 else ret


if __name__ == "__main__":
    import doctest
    doctest.testmod()
