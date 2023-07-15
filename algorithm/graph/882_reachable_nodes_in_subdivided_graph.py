import heapq
from collections import defaultdict
from typing import List


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        visited, graph = [False] * n, [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        heap, subgraph_visit = [(0, 0)], defaultdict(int)
        while heap:
            dist, node = heapq.heappop(heap)
            if visited[node]:
                continue
            visited[node] = True
            for to, w in graph[node]:
                if maxMoves - dist >= w + 1:
                    subgraph_visit[node, to] = w
                    heapq.heappush(heap, (dist + w + 1, to))
                else:
                    subgraph_visit[node, to] = maxMoves - dist
        res = sum(visited)
        for u, v, w in edges:
            res += min(subgraph_visit[u, v] + subgraph_visit[v, u], w)
        return res
