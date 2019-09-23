"""
64. Minimum Path Sum
Medium

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

#1.
[
  [7,6,3],
  [8,7,2],
  [7,3,1]
]

#1.
[
  [1,3,3],
  [8,7,2],
  [7,3,1]
]

1 2
3 4

7 6
7 4
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """O(N) / O(1)"""
        r, c = len(grid), len(grid[0])
        for i in reversed(range(r)):
            for j in reversed(range(c)):
                if i == r - 1 and j == c - 1: continue
                right = grid[i][j+1] if j + 1 < c else float("inf")
                bottom = grid[i+1][j] if i + 1 < r else float("inf")
                grid[i][j] += min(right, bottom)
        return grid[0][0]
