"""
https://leetcode.com/problems/bitwise-and-of-numbers-range/

201. Bitwise AND of Numbers Range
Medium

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND
of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4

5 0101
6 0110
7 0111
=> 0100

Example 2:

Input: [0,1]
Output: 0

0 0000
1 0001
0
"""

from functools import reduce


class Solution:
    def rangeBitwiseAnd4(self, m: int, n: int, i: int = 0) -> int:
        """Check left most bits. O(1) / O(1)"""
        return n << i if m == n else self.rangeBitwiseAnd4(m >> 1, n >> 1, i + 1)

    def rangeBitwiseAnd3(self, m: int, n: int) -> int:
        """Check left most bits. O(1) / O(1)"""
        i = 0
        while m != n:
            m, n = m >> 1, n >> 1
            i += 1
        return n << i

    def rangeBitwiseAnd2(self, m: int, n: int) -> int:
        """O(1) / O(1)"""
        ret = 0
        for bit in reversed(range(32)):
            lower, upper = 1 << bit, 1 << (bit + 1)
            if lower <= m and n < upper:
                ret |= 1 << bit
                m ^= 1 << bit
                n ^= 1 << bit
        return ret

    def rangeBitwiseAnd1(self, m: int, n: int) -> int:
        """O(N) / O(1)"""
        return reduce(lambda x, y: x & y, range(m, n + 1))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
