"""
https://leetcode.com/problems/ugly-number-ii/

264. Ugly Number II
Medium

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """O(N) / O(N)"""
        l, i2, i3, i5 = [1], 0, 0, 0
        while len(l) < n:
            u2, u3, u5 = l[i2] * 2, l[i3] * 3, l[i5] * 5
            l.append(min(u2, u3, u5))
            if l[-1] == u2: i2 += 1
            if l[-1] == u3: i3 += 1
            if l[-1] == u5: i5 += 1
        return l[n - 1]
