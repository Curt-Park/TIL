import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph, costs = defaultdict(dict), dict()
        graph[src][src] = 0
        for u, v, w in flights:
            graph[u][v] = w
        heap = [(-1, 0, src)]  # stop, cost, node
        while heap:
            stop, cost, node = heapq.heappop(heap)
            if node in costs and costs[node] <= cost or stop > k:
                continue
            costs[node] = cost
            for v in graph[node]:
                heapq.heappush(heap, (stop + 1, cost + graph[node][v], v))
        if dst not in costs:
            return -1
        return costs[dst]
