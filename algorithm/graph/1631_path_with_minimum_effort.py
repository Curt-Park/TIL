import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for r, row in enumerate(heights):
            for c, e in enumerate(row):
                for (adj_r, adj_c) in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                    if 0 <= adj_r < len(heights) and 0 <= adj_c < len(heights[0]):
                        graph[r, c][adj_r, adj_c] = abs(
                            heights[r][c] - heights[adj_r][adj_c])
        heap, visited = [(0, (0, 0))], dict()
        while heap:
            dist, now = heapq.heappop(heap)
            if now in visited:
                continue
            visited[now] = dist
            for to, diff in graph[now].items():
                if to in visited:
                    continue
                heapq.heappush(heap, (max(dist, diff), to))
        return visited[len(heights)-1, len(heights[0])-1]
