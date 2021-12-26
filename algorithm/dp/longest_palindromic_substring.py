"""
https://leetcode.com/problems/longest-palindromic-substring/

5. Longest Palindromic Substring
Medium

Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """ O(n^2) / O(1) """
        def getPalindrome(s, l, r):
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            return l + 1, r - 1

        loc = (0, -1)
        for i in range(len(s)):
            odd_loc = getPalindrome(s, i, i)
            even_loc = getPalindrome(s, i, i + 1)
            loc = max([loc, odd_loc, even_loc], key=lambda x: x[1]-x[0])
        return s[loc[0]:loc[1]+1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
