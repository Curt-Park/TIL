"""
https://leetcode.com/problems/rotting-oranges/

994. Rotting Oranges
Medium

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.



Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.


Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
"""


class Solution:
    def orangesRottingFaster(self, grid: List[List[int]]) -> int:
        """O(N) / O(N)"""
        rotted, not_rotted = set(), set()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2: rotted.add((r, c))
                elif val == 1: not_rotted.add((r, c))
        n_step = 0
        while not_rotted:
            rotted = {(r + dr, c + dc) for r, c in rotted \
                        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)] \
                            if (r + dr, c + dc) in not_rotted}
            if not rotted: return -1
            not_rotted -= rotted
            n_step += 1
        return n_step

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotted, not_rotted = set(), set()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2: rotted.add((r, c))
                elif val == 1: not_rotted.add((r, c))
        n_step, rot_once = -1, True
        while rot_once:
            rot_once = False
            for r, c in list(rotted):
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if (r + dr, c + dc) in not_rotted:
                        not_rotted.remove((r + dr, c + dc))
                        rotted.add((r + dr, c + dc))
                        rot_once = True
            n_step += 1
        return -1 if not_rotted else n_step
