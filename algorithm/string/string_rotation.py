"""
796. Rotate String
https://leetcode.com/problems/rotate-string/description/
Easy

We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:

* A and B will have length at most 100.
"""


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        """
        >>> s = Solution()
        >>> s.rotateString('abcde', 'cdeab')
        True
        >>> s.rotateString('abcde', 'abcde')
        True
        >>> s.rotateString('abcde', 'abced')
        False
        >>> s.rotateString('aaaaa', 'aaaab')
        False
        >>> s.rotateString('aaaaa', 'aaaa')
        False
        """
        n1, n2 = len(A), len(B)
        if n1 != n2:
            return False

        if B in A + A:
            return True

        return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()
