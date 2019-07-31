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
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        >>> fn = Solution().groupAnagrams
        >>> fn(["eat", "tea", "tan", "ate", "nat", "bat"])
        [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]
        """
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
