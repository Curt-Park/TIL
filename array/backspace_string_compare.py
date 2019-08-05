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


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        """
        >>> fn = Solution().backspaceCompare
        >>> fn("ab#c", "ad#c")
        True
        >>> fn("ab##", "c#d#")
        True
        >>> fn("a##c", "#a#c")
        True
        >>> fn("a#c", "b")
        False
        """
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
