"""
https://leetcode.com/problems/coin-change/

322. Coin Change
Medium

You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Note:
You may assume that you have an infinite number of each kind of coin.
  1  2  3  4  5  6  7  8  9  10  11
1 1  2  3  4  5  6  7  8  9  10  11
2    1  2  2  3  3  4  4  5   5   6
5    1  2  2  1  2  2  3  3   2   3
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """O(C*A) / O(A)"""
        dp = [0] + [float("inf")] * amount
        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] = min(dp[a], 1 + dp[a - coin])
        return [-1, dp[amount]][dp[amount] != float("inf")]
