"""
https://leetcode.com/problems/course-schedule/

207. Course Schedule
Medium

There are a total of n courses you have to take,
labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course
0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs,
is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0.
             So it is possible.

Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0,
             and to take course 0 you should
             also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges,
not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""

from typing import List


class Solution:
    def canFinish(
            self, numCourses: int, prerequisites: List[List[int]]
    ) -> bool:
        """ O(|V|+|E|), O(|V|+|E|)
        >>> fn = Solution().canFinish
        >>> fn(2, [[1, 0]])
        True
        >>> fn(2, [[1, 0], [0, 1]])
        False
        >>> fn(3, [[2, 1], [1, 0], [2, 0]])
        True
        """
        is_visited = [0 for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]
        for pair in prerequisites: graph[pair[1]].append(pair[0])

        def hasCycle(node: int) -> bool:
            if is_visited[node] in {1, 2}: return is_visited[node] == 2
            is_visited[node] = 2  # on the current path
            if any(hasCycle(v) for v in graph[node]): return True
            is_visited[node] = 1  # visited node
            return False

        return all(not hasCycle(i) for i in range(numCourses))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
