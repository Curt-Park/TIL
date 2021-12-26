"""
https://leetcode.com/problems/group-anagrams/
49. Group Anagrams
Medium

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
All inputs will be in lowercase.
The order of your output does not matter.
"""

from typing import List


class Solution:
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        """O(N), O(N): N is the total number of characters in strs.
        >>> fn = Solution().groupAnagrams2
        >>> fn(["eat", "tea", "tan", "ate", "nat", "bat"])
        [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]
        """
        def getKey(s: str) -> str:
            key = [0] * 26
            for ch in s:
                key[ord(ch) - ord("a")] += 1
            return tuple(key)
        
        dic = {}   
        for s in strs:
            key = getKey(s)
            if key in dic:
                dic[key].append(s)
            else:
                dic[key] = [s]
        return list(dic.values())
        
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        """O(NMlogM), O(NM): N is the string number and M is max str len.
        >>> fn = Solution().groupAnagrams1
        >>> fn(["eat", "tea", "tan", "ate", "nat", "bat"])
        [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]
        """
        dic = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in dic:
                dic[key].append(s)
            else:
                dic[key] = [s]
        return list(dic.values())


if __name__ == "__main__":
    import doctest
    doctest.testmod()
