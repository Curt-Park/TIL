"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

121. Best Time to Buy and Sell Stock
Easy

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

       7 1 5 3 6 4
n_max  7 6 6 6 6 4
ret    5 5 3 3 0 0
"""


class Solution:
    def maxProfit2(self, prices: List[int]) -> int:
        """O(N) / O(1)"""
        n_max = ret = 0
        for p in prices[::-1]:
            n_max = max(n_max, p)
            ret = max(ret, n_max - p)
        return ret

    def maxProfit1(self, prices: List[int]) -> int:
        """O(N^2) / O(1)"""
        ret = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[j] < ret: continue
                ret = max(ret, prices[j] - prices[i])
        return ret
