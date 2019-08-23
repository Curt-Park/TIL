"""
https://leetcode.com/problems/evaluate-division/

399. Evaluate Division
Medium

Equations are given in the format A / B = k, where A and B are
variables represented as strings, and k is a real number
(floating point number). Given some queries, return the answers.
If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values,
vector<pair<string, string>> queries , where equations.size() == values.size(),
and the values are positive. This represents the equations.
Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].

The input is always valid.
You may assume that evaluating the queries will result in no division
by zero and there is no contradiction.
"""

from collections import defaultdict
from itertools import permutations
from typing import List


class Solution:
    def calcEquation2(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]],
    ) -> List[float]:
        """ O(|V|^3), O(|V|^2)
        >>> fn = Solution().calcEquation2
        >>> equations = [["a","b"], ["b","c"]]
        >>> values = [2.0, 3.0]
        >>> queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
        >>> fn(equations, values, queries)
        [6.0, 0.5, -1.0, 1.0, -1.0]
        >>> equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
        >>> values = [3.0,4.0,5.0,6.0]
        >>> queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
        >>> fn(equations, values, queries)
        [360.0, 0.00833, 20.0, 1.0, -1.0, -1.0]
        >>> equations = [["a","b"],["c","d"]]
        >>> values = [1.0,1.0]
        >>> queries = [["a","c"],["b","d"],["b","a"],["d","c"]]
        >>> fn(equations, values, queries)
        [-1.0, -1.0, 1.0, 1.0]
        """
        graph, ret = defaultdict(lambda: defaultdict(lambda: None)), []
        for i, (v1, v2) in enumerate(equations):
            graph[v1][v2], graph[v2][v1] = values[i], 1 / values[i]
            graph[v1][v1] = graph[v2][v2] = 1.0
        for i, j, k in permutations(graph, 3):
            if j in graph[i] and k in graph[j]:
                graph[i][k] = graph[i][j] * graph[j][k]
        for n, d in queries:
            ret.append(graph[n][d] if graph[n][d] is not None else -1.0)
        return ret

    def calcEquation1(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]],
    ) -> List[float]:
        """ O(|Query|x|E|^2), O(|V|^2)
        >>> fn = Solution().calcEquation1
        >>> equations = [["a","b"], ["b","c"]]
        >>> values = [2.0, 3.0]
        >>> queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
        >>> fn(equations, values, queries)
        [6.0, 0.5, -1.0, 1.0, -1.0]
        >>> equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
        >>> values = [3.0,4.0,5.0,6.0]
        >>> queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
        >>> fn(equations, values, queries)
        [360.0, 0.00833, 20.0, 1.0, -1.0, -1.0]
        >>> equations = [["a","b"],["c","d"]]
        >>> values = [1.0,1.0]
        >>> queries = [["a","c"],["b","d"],["b","a"],["d","c"]]
        >>> fn(equations, values, queries)
        [-1.0, -1.0, 1.0, 1.0]
        """
        graph, ret = defaultdict(lambda: defaultdict(lambda: None)), []
        for i, (v1, v2) in enumerate(equations):
            graph[v1][v2], graph[v2][v1] = values[i], 1 / values[i]
            graph[v1][v1] = graph[v2][v2] = 1.0

        def setDivision(n: str, d: str) -> bool:
            if graph[n][d] is None and (n, d) not in visited:
                visited.add((n, d))
                for prox in list(graph[n].keys()):
                    if setDivision(prox, d) and setDivision(n, prox):
                        graph[n][d] = graph[n][prox] * graph[prox][d]
            return graph[n][d] is not None

        for n, d in queries:
            visited = set()
            ret.append(graph[n][d] if setDivision(n, d) else -1.0)
        return ret


if __name__ == "__main__":
    import doctest
    doctest.testmod()
