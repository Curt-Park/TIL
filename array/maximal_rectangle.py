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

[1 0 1 0 0]
[2 0 2 1 1]
[3 1 3 2 2]  <<
[4 0 0 3 0]

(3, 0)
(1, 0)
(1, 0) (3, 2)
(1, 0) (2, 2)

"""

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """ O(NM), O(M)
        >>> fn = Solution().maximalRectangle
        >>> fn([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
        6
        >>> fn([])
        0
        >>> fn([["1"]])
        1
        >>> fn([["0","1"],["1","0"]])
        1
        """
        if not matrix:
            return 0
        w, res = len(matrix[0]), 0
        hist, stack = [0] * (w + 1), []
        for r in matrix:
            for i in range(w + 1):
                if i != w:
                    hist[i] = hist[i] + 1 if r[i] != "0" else 0
                idx = i
                while stack and hist[i] < stack[-1][0]:
                    val, idx = stack.pop()
                    res = max(res, val * (i - idx))
                stack.append((hist[i], idx))
        return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
