"""2045. Second Minimum Time to Reach Destination

Hard
https://leetcode.com/problems/second-minimum-time-to-reach-destination/
"""

import collections
from typing import List


class Solution:
    def secondMinimum(
        self, n: int, edges: List[List[int]], time: int, change: int
    ) -> int:
        """O(|V| + |E|) / O(|V| + |E|).

        Notes:
            - no need to visit the same node at the same time
            - Second shortest path cannot visit the same node 3 times
        """
        graph = [[] for _ in range(n + 1)]
        for v, w in edges:
            graph[v].append(w)
            graph[w].append(v)

        reached, t = False, 0
        queue = collections.deque([(1, t)])  # start from 1
        visited_at = [-1 for _ in range(n + 1)]
        visited_cnt = [0 for _ in range(n + 1)]
        while queue:
            v, t = queue.popleft()
            if visited_at[v] == t or visited_cnt[v] > 1:
                continue
            visited_at[v] = t
            visited_cnt[v] += 1
            if v == n and reached:
                break
            if v == n and not reached:
                reached = True
            is_red, n_changes = (t // change) % 2, t // change
            t = is_red and (n_changes + 1) * change or t
            queue += [(w, t + time) for w in graph[v]]
        return t
