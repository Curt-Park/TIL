"""
https://leetcode.com/problems/power-of-four/

342. Power of Four
Easy

665

236

Add to List

Share
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        """O(1) / O(1)"""
        return num > 0 and num & (num - 1) == 0 and num.bit_length() % 2

    def isPowerOfFourRecursion(self, num: int) -> bool:
        """O(1) / O(1)"""
        if num <= 0 or num & (num - 1) != 0:
            return False
        return num == 1 or self.isPowerOfFourRecursion(num >> 2)
