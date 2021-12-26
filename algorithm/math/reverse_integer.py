"""
https://leetcode.com/problems/reverse-integer/

7. Reverse Integer
Easy

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store
integers within the 32-bit signed integer range: [−2^31,  2^31 − 1].
For the purpose of this problem, assume that your function returns 0
when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x: int) -> int:
        """O(logx) / O(1)"""
        ret, sign, x = 0, x > 0, abs(x)
        while x:
            x, r = divmod(x, 10)
            ret = ret * 10 + r
            if 2**31 - sign < ret: return 0
        return ret * [-1, 1][sign]
