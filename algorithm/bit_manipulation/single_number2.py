"""
https://leetcode.com/problems/single-number-ii/

137. Single Number II
Medium

Given a non-empty array of integers, every element appears
three times except for one, which appears exactly once.
Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3

Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99

1 2 3 1

0001 1111
0011 1101
0000 1110
0001 1111

"""

from typing import List


class Solution:
    def singleNumber4(self, nums: List[int]) -> int:
        """O(N) / O(1)"""
        one = two = bitmask = 0
        for n in nums:
            one, two = one ^ n, two | (one & n)
            bitmask = ~(one & two)
            one, two = one & bitmask, two & bitmask
        return one

    def singleNumber3(self, nums: List[int]) -> int:
        """O(N) / O(1)"""
        bitmask, res = [0] * 32, 0
        for i in range(32):
            for n in nums:
                bitmask[i] += (n >> i) & 1
            res |= (bitmask[i] % 3) << i
        return res - (1 << 32) if (res >> 31) & 1 else res

    def singleNumber2(self, nums: List[int]) -> int:
        """O(N) / O(1)"""
        once = twice = 0
        for n in nums:
            once = ~twice & (once ^ n)
            twice = ~once & (twice ^ n)
        return once

    def singleNumber1(self, nums: List[int]) -> int:
        """O(N) / O(N)"""
        seen, res = set(), 0
        for n in nums:
            if n not in seen:
                seen.add(n)
                res ^= n
            else:
                seen.remove(n)
        return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
