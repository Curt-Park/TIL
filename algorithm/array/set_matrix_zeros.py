"""
73. Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/description/
(Medium)

Share
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        >>> s = Solution()
        >>> s.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        >>> s.setZeroes([[0, 1, 2 ,0], [3, 4 ,5, 2], [1, 3, 1, 5]])
        [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
        >>> s.setZeroes([[1, 0, 2, 3]])
        [[0, 0, 0, 0]]
        >>> s.setZeroes([[0]])
        [[0]]
        >>> s.setZeroes([[]])
        [[]]
        """
        m = len(matrix)
        if m < 1:
            return matrix

        n = len(matrix[0])
        if n < 1:
            return matrix

        # Check the most left and top positions have any zero
        rowHasZero, colHasZero = False, False
        for i in range(m):
            if matrix[i][0] == 0:
                rowHasZero = True
                break

        for j in range(n):
            if matrix[0][j] == 0:
                colHasZero = True
                break

        # Most left and top positions used for zero-flags
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0

        # Mark inner positions according to zero-flags
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if rowHasZero:
            for i in range(m):
                matrix[i][0] = 0

        if colHasZero:
            for j in range(n):
                matrix[0][j] = 0

        return matrix


if __name__ == "__main__":
    import doctest
    doctest.testmod()
