"""
https://leetcode.com/problems/pascals-triangle-ii/

119. Pascal's Triangle II
Easy

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""


class Solution:
    def getRowIter(self, rowIndex: int) -> List[int]:
        """O(N^2), O(N)"""
        row = [1]
        for _ in range(rowIndex):
            row = [x, y for x, y in zip([0] + prevRow, prevRow + [0])]
        return row

    def getRowRec2(self, rowIndex: int) -> List[int]:
        """O(N^2), O(N)"""
        if rowIndex == 0: return [1]
        prevRow = self.getRowRec2(rowIndex - 1)
        return [x + y for x, y in zip([0] + prevRow, prevRow + [0])]

    def getRowRec(self, rowIndex: int) -> List[int]:
        """O(N^2), O(N)"""
        if rowIndex == 0: return [1]
        prevRow = self.getRowRec(rowIndex - 1)
        return [1] + [prevRow[i-1] + prevRow[i] for i in range(1, rowIndex)] + [1]
