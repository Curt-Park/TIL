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
    def longestValidParentheses3(self, s):
        """ O(N), O(1)
        :type s: str
        :rtype: int
        >>> fn = Solution().longestValidParentheses3
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
        n, max_len = len(s), 0

        # left to right scan
        left = right = 0
        for i in range(n):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                max_len = max(max_len, left * 2)
            elif left < right:
                left = right = 0

        # right to left scan
        left = right = 0
        for i in reversed(range(n)):
            if s[i] == ')':
                right += 1
            else:
                left += 1

            if left == right:
                max_len = max(max_len, right * 2)
            elif left > right:
                left = right = 0

        return max_len

    def longestValidParentheses2(self, s):
        """ O(N), O(N)
        :type s: str
        :rtype: int
        >>> fn = Solution().longestValidParentheses2
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
        n = len(s)
        stack, cnt, max_cnt = [], [0] * (n + 1), 0

        for i in range(1, n + 1):
            if s[i - 1] == '(':
                stack.append(i)
            elif stack:
                left = stack.pop()
                cnt[i] = i - left + 1 + cnt[left - 1]
                max_cnt = max(max_cnt, cnt[i])

        return max_cnt

    def longestValidParentheses1(self, s):
        """ O(N), O(N)
        :type s: str
        :rtype: int
        >>> fn = Solution().longestValidParentheses1
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
        n = len(s)
        stack, valid = [], [False] * n

        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif stack:
                valid[stack.pop()], valid[i] = True, True

        max_cnt, cnt = 0, 0
        for i in range(n):
            if valid[i]:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 0

        return max(max_cnt, cnt)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
