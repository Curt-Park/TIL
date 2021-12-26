"""
https://leetcode.com/problems/sum-of-two-integers/

371. Sum of Two Integers
Easy

Calculate the sum of two integers a and b,
but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3

Example 2:

Input: a = -2, b = 3
Output: 1

x y add  carry
0 0  0     0
0 1  1     0
1 0  1     0
1 1  0     1

add = x ^ y
carry = x & y
"""


class Solution:
    def getSum2(self, a: int, b: int) -> int:
        """O(1) / O(1)"""
        mask, sign = 0xffffffff, 0x80000000
        if b: return self.getSum2((a ^ b) & mask, (a & b) << 1)
        return ~(a ^ mask) if a & sign else a

    def getSum1(self, a: int, b: int) -> int:
        """O(1) / O(1)"""
        mask, sign = 0xffffffff, 0x80000000
        while b: a, b = (a ^ b) & mask, (a & b) << 1
        return ~(a ^ mask) if a & sign else a
