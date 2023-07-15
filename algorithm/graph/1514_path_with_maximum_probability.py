import heapq
from typing import List


class Solution:
    def maxProbability(
        self, n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        graph, probs = [[] for _ in range(n)], [0.0] * n
        for (u, v), p in zip(edges, succProb):
            graph[u].append((v, p))
            graph[v].append((u, p))
        heap = [(-1.0, start_node)]
        while heap:
            prob, node = heapq.heappop(heap)
            prob *= -1
            if probs[node] != 0.0:
                continue
            probs[node] = prob
            for to, p in graph[node]:
                if probs[to] != 0.0:
                    continue
                heapq.heappush(heap, (-prob * p, to))
        return probs[end_node]
