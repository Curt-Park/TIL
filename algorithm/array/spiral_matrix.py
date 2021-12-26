"""
https://leetcode.com/problems/spiral-matrix/

54. Spiral Matrix
Medium

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Example 3:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ],
 [ 10,11,12 ],
]
Output: [1,2,3,6,9,12,11,10,7,4,5,8]
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """O(MN) / O(1)"""
        ret, r, c = [], len(matrix), len(matrix[0]) if matrix else 0
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cnt = i = j = idx = 0
        while cnt < r * c:
            ret.append(matrix[i][j])
            matrix[i][j], cnt = None, cnt + 1
            n_i, n_j = i + move[idx][0], j + move[idx][1]
            if not (0 <= n_i < r and 0 <= n_j < c)\
            or matrix[n_i][n_j] is None:
                idx = (idx + 1) % 4
                n_i, n_j = i + move[idx][0], j + move[idx][1]
            i, j = n_i, n_j
        return ret
