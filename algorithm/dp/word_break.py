"""
https://leetcode.com/problems/word-break/

139. Word Break
Medium

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

c a t s a n d o g
    v w     vw

catsandog

1.
cat sandog
    sand og
cats andog
     and og
"""

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(lambda: TrieNode())
        self.terminal = False


class Solution:
    def wordBreak2(self, s, words):
        """O(N^2) / O(N)"""
        ok = [True]
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in words for j in range(i)),
        return ok[-1]

    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        """O(N^2) / O(N)"""
        trie = TrieNode()
        for w in wordDict:
            parent = trie
            for ch in w: parent = parent.children[ch]
            parent.terminal = True

        visit, stack = set(), [0]
        while stack:
            pos, node = stack.pop(), trie
            visit.add(pos)
            while pos < len(s):
                if s[pos] not in node.children: break
                node, pos = node.children[s[pos]], pos + 1
                if node.terminal:
                    if pos == len(s): return True
                    if pos not in visit: stack.append(pos)
        return False
