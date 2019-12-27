"""
https://leetcode.com/problems/couples-holding-hands/

765. Couples Holding Hands
Hard

N couples sit in 2N seats arranged in a row and want to hold hands.
We want to know the minimum number of swaps so that every couple is sitting side by side.
A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1,
the couples are numbered in order, the first couple being (0, 1),
the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

Example 1:
Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.

Example 2:
Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.

Note:
len(row) is even and in the range of [4, 60].
row is guaranteed to be a permutation of 0...len(row)-1.
"""


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        """O(N) / O(N)"""
        self.par = [i - (i % 2) for i in range(len(row))]
        self.rank, swap = [0] * len(row), 0
        for i in range(0, len(row), 2):
            p1, p2 = row[i], row[i + 1]
            c1, c2 = p1 // 2, p2 // 2
            swap += c1 != c2 and self.union(p1, p2)
        return swap

    def find(self, x: int) -> int:
        if self.par[x] == x: return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int)  -> bool:
        x, y = self.find(x), self.find(y)
        if x == y: return False
        if self.rank[x] < self.rank[y]: self.par[x] = y
        elif self.rank[y] < self.rank[x]: self.par[y] = x
        else: self.par[x], self.rank[y] = y, self.rank[y] + 1
        return True
