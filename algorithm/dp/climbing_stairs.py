"""
https://leetcode.com/problems/climbing-stairs/

70. Climbing Stairs
Easy

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


class Solution:
    def climbStairs2(self, n: int) -> int:
        """O(N) / O(1)"""
        a, b =  1, 0
        for _ in range(n):
            a, b = a + b, a
        return a

    def climbStairs1(self, n: int) -> int:
        """O(N) / O(N)"""
        ways = [0] * n + [1, 0]
        for i in reversed(range(n)):
            ways[i] += ways[i + 1] + ways[i + 2]
        return ways[0]
