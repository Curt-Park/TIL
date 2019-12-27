"""
https://leetcode.com/problems/similar-string-groups

839. Similar String Groups
Hard

Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list A of strings.  Every string in A is an anagram of every other string in A.  How many groups are there?

Example 1:
Input: A = ["tars","rats","arts","star"]
Output: 2

Constraints:
1 <= A.length <= 2000
1 <= A[i].length <= 1000
A.length * A[i].length <= 20000
All words in A consist of lowercase letters only.
All words in A have the same length and are anagrams of each other.
The judging time limit has been increased for this question.
"""

import collections, itertools


class Solution:
    def numSimilarGroups2(self, A: List[str]) -> int:
        """O(N^2W or NW^2) / O(NW^3)"""
        self.par, self.rank = list(range(len(A))), [0] * len(A)
        N, W, ans = len(A), len(A[0]), len(A)
        if N < W * W: # If few words, then check for pairwise similarity: O(N^2W)
            for (i1, word1), (i2, word2) in itertools.combinations(enumerate(A), 2):
                ans -= self.isSimilar(word1, word2) and self.union(i1, i2)
        else: # If short words, check all neighbors: O(NW^2)
            buckets = collections.defaultdict(set)
            for i, word in enumerate(A):
                L = list(word)
                for j0, j1 in itertools.combinations(range(W), 2):
                    L[j0], L[j1] = L[j1], L[j0]
                    buckets["".join(L)].add(i)
                    L[j0], L[j1] = L[j1], L[j0]
            for i1, word in enumerate(A):
                for i2 in buckets[word]:
                    ans -= self.union(i1, i2)
        return ans

    def numSimilarGroups1(self, A: List[str]) -> int:
        """O(WN^2) / O(N): Time Limit Exceeds"""
        self.par, self.rank = list(range(len(A))), [0] * len(A)
        ans = len(A)
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if self.par[i] == self.par[j]: continue
                ans -= self.isSimilar(A[i], A[j]) and self.union(i, j)
        return ans

    def isSimilar(self, s1: str, s2: str, n: int = 0) -> bool:
        for i in range(len(s1)):
            if s1[i] != s2[i]: n += 1
            if n > 2: return False
        return True

    def find(self, x: int) -> int:
        if self.par[x] == x: return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int)  -> bool:
        x, y = self.find(x), self.find(y)
        if x == y: return False
        if self.rank[x] < self.rank[y]: self.par[x] = y
        elif self.rank[y] < self.rank[x]: self.par[y] = x
        else: self.par[x], self.rank[y] = y, self.rank[y] + 1
        return True
