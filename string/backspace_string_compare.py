"""
https://leetcode.com/problems/backspace-string-compare/
844. Backspace String Compare
Easy

Given two strings S and T, return if they are equal when both are typed into
empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:
1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.

Follow up:
Can you solve it in O(N) time and O(1) space?
"""

from typing import List


class Solution:
    def backspaceCompare2(self, S: str, T: str) -> bool:
        """O(N), O(1)
        >>> fn = Solution().backspaceCompare2
        >>> fn("ab#c", "ad#c")
        True
        >>> fn("ab##", "c#d#")
        True
        >>> fn("a##c", "#a#c")
        True
        >>> fn("a#c", "b")
        False
        >>> fn("y#fo##f", "y#f#o##f")
        True
        >>> fn("bxj##tw", "bxj###tw")
        False
        >>> fn("nzp#o#g", "b#nzp#o#g")
        True
        """
        def nextIdx(s: str, i: int) -> int:
            cnt = 0
            while i >= 0 and (s[i] == '#' or cnt > 0):
                cnt += 1 if s[i] == '#' else -1
                i -= 1
            return i

        i, j = len(S) - 1, len(T) - 1
        while i >= 0 and j >= 0:
            i, j = nextIdx(S, i), nextIdx(T, j)
            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
                i, j = i - 1, j - 1
        return nextIdx(S, i) < 0 and nextIdx(T, j) < 0

    def backspaceCompare1(self, S: str, T: str) -> bool:
        """ O(N), O(N)
        >>> fn = Solution().backspaceCompare1
        >>> fn("ab#c", "ad#c")
        True
        >>> fn("ab##", "c#d#")
        True
        >>> fn("a##c", "#a#c")
        True
        >>> fn("a#c", "b")
        False
        >>> fn("y#fo##f", "y#f#o##f")
        True
        """
        def backspaceStr(s: str) -> List[str]:
            stack = []
            for c in s:
                if c == '#' and stack:
                    stack.pop()
                elif c != '#':
                    stack.append(c)
            return stack
        return backspaceStr(S) == backspaceStr(T)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
