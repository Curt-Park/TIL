"""
https://leetcode.com/problems/game-of-life/

289. Game of Life
Medium

According to the Wikipedia's article: "The Game of Life, also known simply as Life,
is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using
the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.
The next state is created by applying the above rules simultaneously to every cell in the current state,
where births and deaths occur simultaneously.

Example:

Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]

Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]


Could you solve it in-place? Remember that the board needs to be updated at the same time:
You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array.
In principle, the board is infinite, which would cause problems when the active area
encroaches the border of the array. How would you address these problems?
"""

from itertools import product


class Solution:
    def gameOfLife2(self, board: List[List[int]]) -> None:
        """O(MN) / O(1)
        Do not return anything, modify board in-place instead.
        """
        offset, r, c = [-1, 0, 1], len(board), len(board[0])
        neighbors = [(a, b) for a, b in product(offset, offset) if not a == b == 0]
        for i, j in product(range(r), range(c)):
            count = 0
            for a, b in neighbors:
                if 0 <= i + a < r and 0 <= j + b < c\
                and board[i + a][j + b] in {-1, 1}: count += 1
            if board[i][j] and not 2 <= count <= 3: board[i][j] = -1
            elif not board[i][j] and count == 3:    board[i][j] = 2
        for i, j in product(range(r), range(c)):
            if board[i][j] == -1:  board[i][j] = 0
            elif board[i][j] == 2: board[i][j] = 1

    def gameOfLife1(self, board: List[List[int]]) -> None:
        """O(MN) / O(MN)
        Do not return anything, modify board in-place instead.
        """
        offset, r, c = [-1, 0, 1], len(board), len(board[0])
        neighbors = [(a, b) for a, b in product(offset, offset) if not a == b == 0]
        copy = [[board[i][j] for j in range(c)] for i in range(r)]
        for i, j in product(range(r), range(c)):
            count = 0
            for a, b in neighbors:
                if 0 <= i + a < r and 0 <= j + b < c: count += copy[i + a][j + b]
            if copy[i][j] and not 2 <= count <= 3: board[i][j] = 0
            elif not copy[i][j] and count == 3:    board[i][j] = 1
