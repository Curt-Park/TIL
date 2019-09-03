"""
https://leetcode.com/problems/divide-two-integers/

29. Divide Two Integers
Medium

Given two integers dividend and divisor, divide two integers
without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3

Example 2:

Input: dividend = 7, divisor = -3
Output: -2

Note:
Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store
integers within the 32-bit signed integer range: [−2^31,  2^31 − 1].
For the purpose of this problem, assume that your function returns
2^31 − 1 when the division result overflows.
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """O(1) / O(1)"""
        quot, tmp, pos = 0, 0, (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        for i in reversed(range(32)):
            if tmp + (divisor << i) <= dividend:
                tmp += divisor << i
                quot |= 1 << i
        if (1 << 31) - pos < quot: return (1 << 31) - 1
        return [-quot, quot][pos]
