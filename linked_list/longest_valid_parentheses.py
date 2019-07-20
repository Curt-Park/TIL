"""
https://leetcode.com/problems/longest-valid-parentheses/
Longest Valid Parentheses
Hard

Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        >>> fn = Solution().longestValidParentheses
        >>> fn("(())()")
        6
        >>> fn("(()))()")
        4
        >>> fn("(()())()")
        8
        >>> fn("((()()(()()")
        4
        >>> fn("))))()(()()")
        4
        >>> fn("((((()(()()")
        4
        >>> fn("()")
        2
        >>> fn("(")
        0
        >>> fn("")
        0
        """
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
