"""
https://leetcode.com/problems/n-queens/

51. N-Queens
Hard

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""


from typing import Set, Tuple


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """O(N!) / O(N)"""
        self.ans = []
        self.solve(n)
        return self.ans

    def solve(
        self, n: int, r: int = 0, queens: Set[Tuple[int, int]] = set()
    ) -> None:
        if r == n:
            self.ans += self.getSolutionList(n, queens),
            return
        for c in range(n):
            if self.isVisitable(r, c, queens):
                queens.add((r, c))
                self.solve(n, r + 1)
                queens.remove((r, c))

    def isVisitable(self, i: int, j: int, queens: Set[Tuple[int, int]]) -> bool:
        return not queens or not any(
            q[0] == i or q[1] == j or abs(q[0] - i) == abs(q[1] - j)
            for q in queens
        )

    def getSolutionList(self, n: int, queens: Set[Tuple[int, int]]) -> List[str]:
        return [
            "".join(["Q" if (i, j) in queens else "." for j in range(n)])
            for i in range(n)
        ]
