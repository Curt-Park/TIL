"""
https://leetcode.com/problems/regions-cut-by-slashes/

959. Regions Cut By Slashes
Medium

In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.
These characters divide the square into contiguous regions.
(Note that backslash characters are escaped, so a \ is represented as "\\".)
Return the number of regions.

Example 1:
Input:
[
  " /",
  "/ "
]

Output: 2
Explanation: The 2x2 grid is as follows:

Example 2:
Input:
[
  " /",
  "  "
]

Output: 1
Explanation: The 2x2 grid is as follows:

Example 3:
Input:
[
  "\\/",
  "/\\"
]

Output: 4
Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
The 2x2 grid is as follows:

Example 4:
Input:
[
  "/\\",
  "\\/"
]

Output: 5
Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\, and "\\/" refers to \/.)
The 2x2 grid is as follows:

Example 5:
Input:
[
  "//",
  "/ "
]
Output: 3
Explanation: The 2x2 grid is as follows:

Note:
1 <= grid.length == grid[0].length <= 30
grid[i][j] is either '/', '\', or ' '.
"""

from itertools import product


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        """O(N^2) / O(N^2)"""
        N = len(grid)
        self.par, self.rank = list(range(N * N * 4)), [0] * (N * N * 4)
        for r, c in product(range(N), range(N)):
            root = 4 * (r * N + c)
            if grid[r][c] != "\\":
                self.union(root, root + 3); self.union(root + 1, root + 2)
            if grid[r][c] != "/":
                self.union(root, root + 1); self.union(root + 2, root + 3)
            if r + 1 < N:  # down
                self.union(root + 2, root + 4 * N)
            if 0 <= r - 1: # up
                self.union(root, root - 4 * N + 2)
            if c + 1 < N: # right
                self.union(root + 1, root + 4 + 3)
            if 0 <= c - 1: # left
                self.union(root + 3, root - 4 + 1)
        return sum(self.find(x) == x for x in range(4 * N * N))

    def find(self, x: int) -> int:
        if self.par[x] == x: return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)
        if self.rank[x] < self.rank[y]: self.par[x] = y
        elif self.rank[y] < self.rank[x]: self.par[y] = x
        else: self.par[x], self.rank[y] = y, self.rank[y] + 1
