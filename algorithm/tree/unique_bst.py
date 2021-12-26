"""
https://leetcode.com/problems/unique-binary-search-trees/

96. Unique Binary Search Trees
Medium

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


class Solution:
    def numTrees(self, n: int, dp = {0: 1, 1: 1}) -> int:
        """O(N^2) / O(N)"""
        return n in dp and dp[n] or dp.setdefault(n, sum(
            self.numTrees(i) * self.numTrees(n - i - 1) for i in range(n)
        ))
