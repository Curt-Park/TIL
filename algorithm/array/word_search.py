"""
https://leetcode.com/problems/word-search/

79. Word Search
Medium

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

from itertools import product


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """O(SMN) / O(S+MN)"""
        def search_word(loc, idx, visit=set()):
            if loc in visit: return False
            if idx == len(word) - 1: return True
            visit.add(loc)
            for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                r, c = loc[0] + i, loc[1] + j
                if 0 <= r < m and 0 <= c < n\
                and (r, c) in dic[word[idx + 1]]\
                and search_word((r, c), idx + 1): return True
            visit.remove(loc)
            return False
        dic, m, n = {ch: set() for ch in word}, len(board), len(board[0])
        for r, c in product(range(m), range(n)):
            if board[r][c] in dic: dic[board[r][c]].add((r, c))
        return any(search_word(loc, 0) for loc in dic[word[0]]) if word else False
