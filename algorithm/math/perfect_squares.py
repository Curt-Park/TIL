"""
https://leetcode.com/problems/perfect-squares/

279. Perfect Squares
Medium

Given a positive integer n, find the least number of
perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

1: 1
2: 1 + 1: 2
3: 1 + 2: 3
4: 1
5: 4 + 1: 2
6: 4 + 2: 3
7: 4 + 3: 4
8: 4 + 4: 2
9: 1
10: 9 + 1: 2
11: 9 + 2: 3
12: (1, 11), (2, 10), (3, 9), ..., (6, 6)
"""

from typing import Dict


class Solution:
    # BFS
    def numSquares3(self, n: int) -> int:
        """O(N) / O(N)"""
        q, visit, cnt = [n], set(), 0
        while q:
            cur, q, cnt = q, [], cnt + 1
            for n in cur:
                for i in range(1, int(n ** 0.5) + 1):
                    child = n - i ** 2
                    if not child: return cnt
                    if child in visit: continue
                    visit.add(child), q.append(child)
        return cnt
    
    # Shortest Path: Bellman-Ford
    def numSquares2(self, n: int) -> int:
        """O(N**2) / O(N)"""
        graph = defaultdict(lambda: float("inf"))
        for i in range(1, int(n ** 0.5) + 1): graph[i**2] = 1
        for v in range(1, n + 1):
            for u in list(graph.keys()):
                graph[v] = min(graph[v], graph[v - u] + graph[u])
        return graph[n]
        
    # Dynamic Programming
    def numSquares1(self, n: int, nums: Dict[int, int] = {}) -> int:
        """O(N) / O(N)"""
        if not n ** 0.5 % 1: nums[n] = 1
        if n in nums: return nums[n]
        fn, end = self.numSquares, int(n ** 0.5) + 1
        nums[n] = min(1 + fn(n - i ** 2) for i in range(1, end))
        return nums[n]
