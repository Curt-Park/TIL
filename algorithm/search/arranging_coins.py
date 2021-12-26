"""Arranging Coins

https://leetcode.com/explore/featured/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3377/

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
Given n, find the total number of full staircase rows that can be formed.
n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
"""

class Solution:
    def arrangeCoins0(self, n: int) -> int:
        """O(N) / O(1)."""
        for i in range(1, n + 2):
            if n < i:
                return i - 1
            n -= i
        return 0

    def arrangeCoins1(self, n: int) -> int:
        """O(N) / O(1)."""
        for i in range(1, n + 2):
            if n < i * (i + 1) // 2:
                return i - 1
        return 0

    def arrangeCoins2(self, n: int) -> int:
        """O(log(N)) / O(1)."""
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            k = mid * (1 + mid) / 2
            if n < k: r = mid - 1
            elif k < n: l = mid + 1
            else: return mid
        return r

    def arrangeCoins3(self, n: int) -> int:
        """O(1) / O(1).

        k(k+1)/2 <= N
        <=> k^2 + k + 1/4 <= 2N + 1/4
        <=> (k + 1/2)^2 <= 2N + 1/4
        <=> k + 1/2 <= sqrt(2N + 1/4)
        <=> k <= sqrt(2N + 1/4) - 1/2
        => k = floor(sqrt(2N + 1/4) - 1/2)
        """
        return int((2 * n + 0.25) ** 0.5 - 0.5)
