"""
https://leetcode.com/problems/sudoku-solver/

37. Sudoku Solver
Hard

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:
The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
"""

import heapq
from itertools import product
from typing import Set


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """O(1) / O(1)
        Do not return anything, modify board in-place instead.
        """
        self.stack, self.board = [], board
        self.boxid = lambda r, c: r // 3 * 3 + c // 3
        self.rows, self.cols, self.boxs = (
            [set() for _ in range(9)] for _ in range(3)
        )
        for i, j in product(range(9), range(9)):
            if self.board[i][j].isdigit():
                self.add_num(i, j, self.board[i][j])
            else: self.stack.append((i, j))
        self.solve()

    def solve(self) -> bool:
        if not self.stack: return True
        i, j = self.stack.pop()
        for n in self.get_candidate(i, j):
            self.add_num(i, j, n)
            if self.solve(): return True
            self.remove_num(i, j)
        self.stack.append((i, j))
        return False

    def add_num(self, i: int, j: int, n: str) -> None:
        self.board[i][j] = n
        self.rows[i].add(n)
        self.cols[j].add(n)
        self.boxs[self.boxid(i, j)].add(n)

    def remove_num(self, i: int, j: int) -> None:
        self.rows[i].remove(self.board[i][j])
        self.cols[j].remove(self.board[i][j])
        self.boxs[self.boxid(i, j)].remove(self.board[i][j])
        self.board[i][j] = "."

    def get_candidate(self, i: int, j: int) -> Set[int]:
        candi = set(str(i) for i in range(1, 10))
        candi -= self.rows[i]
        candi -= self.cols[j]
        candi -= self.boxs[self.boxid(i, j)]
        return candi
