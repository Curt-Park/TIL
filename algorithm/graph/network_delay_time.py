"""
https://leetcode.com/problems/network-delay-time/

743. Network Delay Time
Medium

There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w),
where u is the source node, v is the target node,
and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K.
How long will it take for all nodes to receive the signal?
If it is impossible, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2

Note:
N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
"""

import heapq
from collections import defaultdict
from itertools import permutations
from typing import List


class Solution:
    # Bellman-Ford
    def networkDelayTime3(self, times: List[List[int]], N: int, K: int) -> int:
        """O(|N|*|E|) / O(|V|)"""
        dist = [float("inf") if i != K-1 else 0 for i in range(N)]
        for _ in range(N):
            for u, v, w in times:
                dist[v-1] = min(dist[v-1], dist[u-1] + w)
        return -1 if float("inf") in dist else max(dist)

    # Dijkstra
    def networkDelayTime2(self, times: List[List[int]], N: int, K: int) -> int:
        """O((|E|+|V|)log|V|) / O(|V|)"""
        graph = defaultdict(lambda: defaultdict(lambda: float("inf")))
        visited, heap, graph[K][K] = set(), [(0, K)], 0
        for u, v, w in times: graph[u][v] = w
        while heap:
            u = heapq.heappop(heap)[1]
            visited.add(u)
            for v in [v for v in graph[u] if v not in visited]:
                if graph[K][v] >= graph[K][u] + graph[u][v]:
                    graph[K][v] = graph[K][u] + graph[u][v]
                    heapq.heappush(heap, (graph[K][v], v))
        t = {graph[K][v] for v in range(1, N+1) if v != K}
        return -1 if float("inf") in t else max(t)

    # Floyd-Warshall
    def networkDelayTime1(self, times: List[List[int]], N: int, K: int) -> int:
        """O(N^3) / O(|V|^2)"""
        graph = defaultdict(lambda: defaultdict(lambda: float("inf")))
        for s, e, w in times: graph[s][e] = w
        for k, i, j in permutations(range(1, N+1), 3):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
        t = {graph[K][v] for v in range(1, N+1) if v != K}
        return -1 if float("inf") in t else max(t)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
