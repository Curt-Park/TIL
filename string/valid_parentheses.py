"""
https://leetcode.com/problems/valid-parentheses/
20. Valid Parentheses
Easy

Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
"""


class Solution(object):
    def isValid(self, s):
        """ O(N), O(N)
        :type s: str
        :rtype: bool
        >>> fn = Solution().isValid
        >>> fn("()")
        True
        >>> fn("()[]{}")
        True
        >>> fn("(]")
        False
        >>> fn("([)]")
        False
        >>> fn("{[]}")
        True
        """
        stack = []
        pair = {")": "(", "}": "{", "]": "["}
        for ch in s:
            if ch in pair:
                if not stack or stack[-1] != pair[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
