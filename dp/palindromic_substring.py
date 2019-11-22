"""
647. Palindromic Substrings
Medium

Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Note:
The input string length won't exceed 1000.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        """O(N^2) / O(N)"""
        def count(l: int, r: int) -> int:
            return 0 <= l < r < len(s) and s[l] == s[r] and 1 + count(l-1, r+1)
        return len(s) + sum(count(i-1, i+1) + count(i, i+1) for i in range(len(s)))
