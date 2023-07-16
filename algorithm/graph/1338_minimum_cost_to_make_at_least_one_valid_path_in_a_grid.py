import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        graph = defaultdict(lambda: defaultdict(lambda: float("inf")))
        for r, row in enumerate(grid):
            for c, e in enumerate(row):
                graph[r, c][r, c + 1] = graph[r, c][r, c - 1] = 1
                graph[r, c][r + 1, c] = graph[r, c][r - 1, c] = 1
                graph[r, c][r + (e == 3) - (e == 4), c + (e == 1) - (e == 2)] = 0
        dists = defaultdict(lambda: float("inf"))
        heap = [(0, (0, 0))]
        while heap:
            dist, now = heapq.heappop(heap)
            if now in dists:
                continue
            dists[now] = dist
            for to, w in graph[now].items():
                if to in dists:
                    continue
                heapq.heappush(heap, (dist + w, to))
        return dists[len(grid) - 1, len(grid[0]) - 1]
