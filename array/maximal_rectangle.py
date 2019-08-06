"""
https://leetcode.com/problems/maximal-rectangle/
85. Maximal Rectangle
Hard

Given a 2D binary matrix filled with 0's and 1's,
find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

Output: 6
"""

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        >>> fn = Solution().maximalRectangle
        >>> fn([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
        6
        """
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
