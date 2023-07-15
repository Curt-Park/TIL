from collections import defaultdict
from typing import List


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        graph = defaultdict(lambda: defaultdict(lambda: float("inf")))
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w
        for i in range(n):
            graph[i][i] = 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
        res = (float("inf"), -1)
        for i in range(n):
            n_cities = sum(v <= distanceThreshold for v in graph[i].values())
            if n_cities <= res[0]:
                res = (n_cities, i)
        return res[1]
