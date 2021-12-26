"""
https://leetcode.com/problems/minimum-height-trees/

310. Minimum Height Trees
Medium

For an undirected graph with tree characteristics,
we can choose any node as the root. The result graph is then a rooted tree.
Among all possible rooted trees, those with minimum height are called
minimum height trees (MHTs). Given such a graph, write a function to find
all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1.
You will be given the number n and a list of undirected edges
(each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0, 1] is the same as [1, 0] and
thus will not appear together in edges.

Example 1 :
Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3

Output: [1]

Example 2 :
Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5

Output: [3, 4]

Note:
According to the definition of tree on Wikipedia: “a tree is an undirected
graph in which any two vertices are connected by exactly one path.
In other words, any connected graph without simple cycles is a tree.”
The height of a rooted tree is the number of edges on the longest downward
path between the root and a leaf.
"""

from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """O(N) / O(N)
        >>> fn = Solution().findMinHeightTrees
        >>> fn(4, [[1, 0], [1, 2], [1, 3]])
        [1]
        >>> fn(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])
        [3, 4]
        """
        graph = {v: set() for v in range(n)}
        for f, t in edges: graph[f].add(t), graph[t].add(f)
        q, next_q = [v for v in range(n) if len(graph[v]) < 2], []   
        while q:
            for v in q:
                for w in graph[v]:
                    graph[w].remove(v)
                    if len(graph[w]) == 1: next_q.append(w)
            ret, q, next_q = q, next_q, []
        return ret
        
        
if __name__ =="__main__":
    import doctest
    doctest.testmod()
