"""
https://leetcode.com/problems/regular-expression-matching/

10. Regular Expression Matching
Hard

Given an input string (s) and a pattern (p),
implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z,
and characters like . or *.

Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element,
'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time.
Therefore, it matches "aab".

Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        >>> fn = Solution().isMatch
        >>> fn(s = "aa", p = "a")
        False
        >>> fn(s = "aa", p = "a*")
        True
        >>> fn(s = "ab",  p = ".*")
        True
        >>> fn(s = "aab",  p = "c*a*b")
        True
        >>> fn(s = "mississippi", p = "mis*is*p*.")
        False
        """
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
