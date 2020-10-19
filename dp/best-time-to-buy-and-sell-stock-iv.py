"""
188. Best Time to Buy and Sell Stock IV
Hard

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
Design an algorithm to find the maximum profit. You may complete at most k transactions.
Notice that you may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.


Constraints:

0 <= k <= 109
0 <= prices.length <= 104
0 <= prices[i] <= 1000
"""


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """O(KN) / O(K)"""
        # memory exeeds without this statement
        if k >= len(prices) / 2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
        sell, buy = [0] * (k + 1), [float("inf")] * (k + 1)
        for i in range(len(prices)):
            for j in range(1, k + 1):
                buy[j] = min(buy[j], prices[i] - sell[j - 1])
                sell[j] = max(sell[j], prices[i] - buy[j])
        return sell[k]

    def maxProfit(self, k: int, prices: List[int]) -> int:
        """O(KN) / O(KN)

        DP Formula:
            dp[k, i] = max(dp[k, i-1], prices[i] - prices[j] + dp[k-1, j-1]), j=[0..i-1]
        """
        if k >= len(prices) / 2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
        dp = dict()
        for i in range(k):
            m, dp[i, 0] = prices[0], 0
            for j in range(1, len(prices)):
                m = min(m, prices[j] - dp.get((i - 1, j - 1), 0))
                dp[i, j] = max(dp[i, j - 1], prices[j] - m)
        return int(k > 0) and dp[k - 1, len(prices) - 1]
