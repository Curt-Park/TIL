"""Island Perimeter

https://leetcode.com/problems/island-perimeter/

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:
https://assets.leetcode.com/uploads/2018/10/12/island.png
"""


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """O(M+N) / O(1)"""
        if not grid or not grid[0]: return 0
        perimeter, h, w = 0, len(grid), len(grid[0])
        for r in range(h):
            for c in range(w):
                if not grid[r][c]: continue
                n_stripes = 4
                if r > 0 and grid[r-1][c] == 1: n_stripes -= 1 # top
                if c < w - 1 and grid[r][c+1] == 1: n_stripes -= 1 # right
                if r < h - 1 and grid[r+1][c] == 1: n_stripes -= 1 # bottom
                if c > 0 and grid[r][c-1] == 1: n_stripes -= 1 # left
                perimeter += n_stripes
        return perimeter
