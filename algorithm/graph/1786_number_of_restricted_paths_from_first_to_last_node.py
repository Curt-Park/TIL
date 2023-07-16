import heapq
from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w
        heap, dists = [(0, n)], dict()
        while heap:
            dist, now = heapq.heappop(heap)
            if now in dists:
                continue
            dists[now] = dist
            for to, w in graph[now].items():
                if to in dists:
                    continue
                heapq.heappush(heap, (dist + w, to))

        @cache
        def dfs(node) -> int:
            if node == n:
                return 1
            ans = 0
            for next_node in graph[node]:
                if dists[node] > dists[next_node]:
                    ans += dfs(next_node)
            return ans

        return dfs(1) % 1_000_000_007
