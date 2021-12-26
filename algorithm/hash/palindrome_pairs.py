"""
https://leetcode.com/problems/palindrome-pairs/
336. Palindrome Pairs
Hard

Given a list of unique words, find all pairs of
distinct indices (i, j) in the given list,
so that the concatenation of the two words,
i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
"""


from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """ O(NM^2), O(N)
        >>> fn = Solution().palindromePairs
        >>> fn(["abcd","dcba","lls","s","sssll"])
        [[0, 1], [1, 0], [2, 4], [3, 2]]
        >>> fn(["bat","tab","cat"])
        [[0, 1], [1, 0]]
        >>> fn(["","a"])
        [[0, 1], [1, 0]]
        """
        lookup, ret = {w: i for i, w in enumerate(words)}, []
        for i, w in enumerate(words):
            m = len(w)
            for j in range(m + 1):
                pre, post = w[:j], w[j:]
                rev_pre, rev_post = pre[::-1], post[::-1]
                if pre == rev_pre and rev_post in lookup and lookup[rev_post] != i:
                    ret.append([lookup[rev_post], i])
                if j != m and post == rev_post and rev_pre in lookup:
                    ret.append([i, lookup[rev_pre]])
        return ret


if __name__ == "__main__":
    import doctest
    doctest.testmod()
