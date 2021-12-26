"""
74. Search a 2D Matrix
Medium

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.


Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
Output: false
Example 3:

Input: matrix = [], target = 0
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
0 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""

import bisect


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """O(logM + logN) / O(1)"""
        r_idx = bisect.bisect([r[0] for r in matrix if r], target) - 1
        row = matrix[r_idx] if 0 <= r_idx < len(matrix) else []
        c_idx = bisect.bisect_left(row, target)
        return c_idx < len(row) and target == row[c_idx]
