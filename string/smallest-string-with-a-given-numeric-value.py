"""
https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

1663. Smallest String With A Given Numeric Value
Medium

The numeric value of a lowercase character is defined as its position (1-indexed) in the alphabet, so the numeric value of a is 1, the numeric value of b is 2, the numeric value of c is 3, and so on.

The numeric value of a string consisting of lowercase characters is defined as the sum of its characters' numeric values. For example, the numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.

You are given two integers n and k. Return the lexicographically smallest string with length equal to n and numeric value equal to k.

Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.



Example 1:

Input: n = 3, k = 27
Output: "aay"
Explanation: The numeric value of the string is 1 + 1 + 25 = 27, and it is the smallest string with such a value and length equal to 3.
Example 2:

Input: n = 5, k = 73
Output: "aaszz"


Constraints:

1 <= n <= 105
n <= k <= 26 * n
"""


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        """O(N) / O(N)"""
        d = {k: ch for k, ch in enumerate("abcdefghijklmnopqrstuvwxyz")}
        s, k, i = ["a"] * n, k - n, n - 1
        while k > 0:
            ch = min(25, k)
            s[i] = d[ch]
            k -= ch
            i -= 1
        return "".join(s)

    dp = {(1, k): chr(k - 1 + ord('a')) for k in range(1, 27)}
    def getSmallestString(self, n: int, k: int) -> str:
        """MLE"""
        if k > n * 26:
            return ""
        if (n, k) in self.dp:
            return self.dp[n, k]
        for i in range(1, 27):
            pre = chr(i - 1 + ord('a'))
            post = self.getSmallestString(n - 1, k - i)
            if len(post) == n - 1:
                self.dp[n, k] = pre + post
                return self.dp[n, k]
        return ""

    def getSmallestString(self, n: int, k: int) -> str:
        """TLE"""
        if k > n * 26:
            return ""
        if n == 1 and k <= 26:
            return chr(k - 1 + ord('a'))
        for i in range(1, 27):
            pre = chr(i - 1 + ord('a'))
            post = self.getSmallestString(n - 1, k - i)
            if len(post) == n - 1:
                return pre + post
        return ""
