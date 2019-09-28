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

import re


class Solution:
    def ismatch(self, s: str, p: str) -> bool:
        """O(|S|*|P|) / O(|S|*|P|)"""
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(2, n + 1):
            dp[0][i] = p[i - 1] == '*' and dp[0][i - 2];
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] != '*':
                    dp[i][j] = dp[i - 1][j - 1] and p[j - 1] in {'.', s[i - 1]}
                else:
                    dp[i][j] = dp[i][j - 2] or p[j - 2] in {'.', s[i - 1]} and dp[i - 1][j]
        return dp[m][n]
        # return re.match(p, s).span() == (0, len(s))
