"""
https://leetcode.com/problems/find-the-town-judge/

997. Find the Town Judge
Easy

In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:
The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3

Note:
1 <= N <= 1000
trust.length <= 10000
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N
"""


from collections import defaultdict


class Solution:
    def findJudge2(self, N: int, trust: List[List[int]]) -> int:
        """O(|E|) / O(|V|)"""
        cnt, trust_sb, ans = [0] * N, set(), 1
        for s, t in trust:
            trust_sb.add(s)
            cnt[t - 1] += 1
            if cnt[t - 1] == N - 1: ans = t
        return ans not in trust_sb and ans or -1

    def findJudge1(self, N: int, trust: List[List[int]]) -> int:
        """O(|V|+|E|) / O(|V|+|E|)"""
        def traverse(i: int) -> None:
            if i in visited: return
            visited.add(i)
            for next_idx in graph[i]:
                cnt[next_idx] += 1
                traverse(next_idx)
        if N == 1 and not trust: return 1
        graph, cnt, visited = defaultdict(lambda: []), defaultdict(lambda: 0), set()
        for s, t in trust: graph[s].append(t)
        for i in range(1, N + 1): traverse(i)
        for i, n in cnt.items():
            if n == N - 1 and len(graph[i]) == 0: return i
        return -1
