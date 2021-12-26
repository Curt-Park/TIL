"""
https://leetcode.com/problems/generate-parentheses/

22. Generate Parentheses
Medium

Given n pairs of parentheses,
write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """O(4^N/SQRT(N)) / O(4^N/SQRT(N))"""
        d = {1: {"()"}}
        for i in range(2, n + 1):
            d[i] = {
                prev[:pos] + "()" + prev[pos:]
                for prev in d[i - 1] for pos in range(len(prev) + 1)
            }
        return list(d[n])
