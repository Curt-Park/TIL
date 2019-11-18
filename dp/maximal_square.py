"""
https://leetcode.com/problems/maximal-square/

221. Maximal Square
Medium

Given a 2D binary matrix filled with 0's and 1's,
find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4

1 0 1 0 0
1 0 1 1 1
1 1 1 2 2
1 0 0 1 0

Input:

[["0","0","0","1"],
["1","1","0","1"],
["1","1","1","1"],
["0","1","1","1"],
["0","1","1","1"]]

0 0 0 1
1 1 0 1
1 2 1 1
0 1 2 2
0 1 2 3

output: 9

[["1","0","1","1","0","1"],
["1","1","1","1","1","1"],
["0","1","1","0","1","1"],
["1","1","1","0","1","0"],
["0","1","1","1","1","1"],
["1","1","0","1","1","1"]]

1 0 1 1 0 1
1 1 1 2 1 1
0 1 2 0 0 2
1 1 2 0 1 0
0 1 2 1 1 1
1 1 0 1 1 2

Output: 4


[[1]]
output 1
"""


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """O(MN) / O(1)"""
        sqrt_ans, dp = 0, matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[i][j] = int(dp[i][j])
                if i and j and dp[i][j]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                sqrt_ans = max(sqrt_ans, dp[i][j])
        return sqrt_ans ** 2
