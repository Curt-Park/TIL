"""
https://leetcode.com/problems/longest-palindrome/

409. Longest Palindrome
Easy

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""


from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        """O(N), O(N)"""
        ret, even, total = 0, 0, 0
        for n in Counter(s).values():
            d, m = divmod(n, 2)
            ret += 2 * d
            total += 1
            even += m == 0
        return ret + int(total != even)
