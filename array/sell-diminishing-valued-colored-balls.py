"""
https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

1648. Sell Diminishing-Valued Colored Balls
Medium

You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.

The customer weirdly values the colored balls. Each colored ball's value is the number of balls of that color you currently have in your inventory. For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow ball. After the transaction, there are only 5 yellow balls left, so the next yellow ball is then valued at 5 (i.e., the value of the balls decreases as you sell more to the customer).

You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color that you initially own. You are also given an integer orders, which represents the total number of balls that the customer wants. You can sell the balls in any order.

Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too large, return it modulo 109 + 7.



Example 1:


Input: inventory = [2,5], orders = 4
Output: 14
Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
The maximum total value is 2 + 5 + 4 + 3 = 14.
Example 2:

Input: inventory = [3,5], orders = 6
Output: 19
Explanation: Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5 + 4 + 3 + 2).
The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.
Example 3:

Input: inventory = [2,8,4,10,6], orders = 20
Output: 110
Example 4:

Input: inventory = [1000000000], orders = 1000000000
Output: 21
Explanation: Sell the 1st color 1000000000 times for a total value of 500000000500000000. 500000000500000000 modulo 109 + 7 = 21.


Constraints:

1 <= inventory.length <= 105
1 <= inventory[i] <= 109
1 <= orders <= min(sum(inventory[i]), 109)
"""


import heapq


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        """O(IlogI) / O(1)"""
        sum_range = lambda b, e: (e - b + 1) * (b + e) // 2
        inventory.sort(reverse=True)
        inventory += [0]
        ans, k = 0, 0
        for i in range(len(inventory) - 1):
            l, r, k = inventory[i], inventory[i + 1], k + 1
            if l == r:  # keep going to find the square
                continue
            if orders <= k * (l - r):  # when it cannot use all the square
                break
            ans += k * sum_range(r + 1, l)  # use the square
            orders -= k * (l - r)
        (q, r), top = divmod(orders, k), inventory[i]
        ans += k * sum_range(top - q + 1, top)
        ans += r * (top - q)
        return ans % (10**9 + 7)

    def maxProfit(self, inventory: List[int], orders: int) -> int:
        """O(OlogI) / O(I): Time limit exceeds."""
        inv, prof = [-n for n in inventory], 0
        heapq.heapify(inv)
        for _ in range(orders):
            n = -heapq.heappop(inv)
            if n == 0:
                break
            prof += n
            heapq.heappush(inv, -n + 1)
        return prof % (10**9 + 7)
