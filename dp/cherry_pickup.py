"""
https://leetcode.com/problems/cherry-pickup/

741. Cherry Pickup
Hard

In a N x N grid representing a field of cherries, each cell is one of three possible integers.

0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.


Your task is to collect maximum number of cherries possible by following the rules below:

Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);
After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.


Example 1:

Input: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
Output: 5

Explanation:
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.

Note:
grid is an N by N 2D array, with 1 <= N <= 50.
Each grid[i][j] is an integer in the set {-1, 0, 1}.
It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.
"""


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """O(N^2) / O(N^2)"""
        def double_search(r1, c1, r2, c2, N=len(grid), dp={}):
            if (r1, c1, r2, c2) in dp:
                return dp[r1, c1, r2, c2];
            if (r1, c1) == (N - 1, N - 1) or (r2, c2) == (N - 1, N - 1):
                return grid[N-1][N-1]
            if N in {r1, c1, r2, c2} or -1 in {grid[r1][c1], grid[r2][c2]}:
                return float("-inf")
            dp[r1, c1, r2, c2] = grid[r1][c1]
            dp[r1, c1, r2, c2] += grid[r2][c2] if (r1, c1) != (r2, c2) else 0
            dp[r1, c1, r2, c2] += max([
                double_search(r1+1, c1, r2+1, c2), double_search(r1+1, c1, r2, c2+1),
                double_search(r1, c1+1, r2+1, c2), double_search(r1, c1+1, r2, c2+1),
            ])
            return dp[r1, c1, r2, c2]
        return max(0, double_search(0, 0, 0, 0))
