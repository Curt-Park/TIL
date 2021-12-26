"""
https://leetcode.com/problems/redundant-connection/

684. Redundant Connection
Medium

In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3

Example 2:
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.

Update (2017-09-26):
We have overhauled the problem description + test cases and specified clearly the graph is an undirected graph. For the directed graph follow up please see Redundant Connection II). We apologize for any inconvenience caused.
"""


from collections import defaultdict


class Solution:
    def findRedundantConnection3(self, edges: List[List[int]]) -> List[int]:
        """O(N^2) / O(N)"""
        root = list(range(len(edges) + 1))
        for u, v in edges:
            if root[u] == root[v]:
                return u, v
            target = root[u]
            for i in range(len(root)):
                if root[i] == target:
                    root[i] = root[v]
        return []

    def findRedundantConnection2(self, edges: List[List[int]]) -> List[int]:
        """O(N) / O(N)
        https://en.wikipedia.org/wiki/Disjoint-set_data_structure#Time_complexity
        """
        def find(x: int) -> int:
            if self.par[x] == x: return x
            self.par[x] = find(self.par[x])
            return self.par[x]
        def union(x: int, y: int) -> bool:
            x, y = find(x), find(y)
            if x == y: return False
            if self.rank[x] < self.rank[y]: self.par[x] = y
            elif self.rank[y] < self.rank[x]: self.par[y] = x
            else: self.par[x], self.rank[y] = y, self.rank[y] + 1
            return True
        self.par, self.rank = list(range(len(edges) + 1)), [0] * (len(edges) + 1)
        for e in edges:
            if not union(*e): return e
        return []

    def findRedundantConnection1(self, edges: List[List[int]]) -> List[int]:
        """O(N^2) / O(N)"""
        def isReachable(v: int, target: int) -> bool:
            if v in visited: return False
            if v == target: return True
            visited.add(v)
            return any(isReachable(adj_v, target) for adj_v in graph[v])
        graph, visited = defaultdict(set), set()
        for s, e in edges:
            visited.clear()
            if {s, e}.issubset(graph) and isReachable(s, e): return s, e
            graph[s].add(e); graph[e].add(s)
        return []
