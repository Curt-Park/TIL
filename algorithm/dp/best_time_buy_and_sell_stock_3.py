"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/


123. Best Time to Buy and Sell Stock III
Hard

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """O(N), O(1)"""
        buy1 = buy2 = float("inf")
        sell1 = sell2 = 0
        for p in prices:
            buy1 = min(buy1, p)
            sell1 = max(sell1, p - buy1)
            buy2 = min(buy2, p - sell1)
            sell2 = max(sell2, p - buy2)
        return sell2

    def maxProfit(self, prices: List[int]) -> int:
        """O(N), O(1)"""
        if not prices: return 0
        dp, m = [0] * 3, [float("inf")] * 3
        for i in range(len(prices)):
            for k in range(1, 3):
                m[k] = min(m[k], prices[i] - dp[k-1])
                dp[k] = max(dp[k], prices[i] - m[k])
        return dp[2]

    def maxProfit(self, prices: List[int]) -> int:
        """O(N), O(N)"""
        if not prices: return 0
        dp = dict()
        for k in range(2):
            m, dp[k, 0] = prices[0], 0
            for i in range(1, len(prices)):
                m = min(m, prices[i] - dp.get((k-1, i-1), 0))
                dp[k, i] = max(dp[k, i-1], prices[i] - m)
        return dp[1, len(prices) - 1]
