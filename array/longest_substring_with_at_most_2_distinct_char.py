"""
https://leetcode.com/explore/interview/card/google/59/array-and-strings/3054/
"""


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """ O(N), O(1)
        >>> fn = Solution().lengthOfLongestSubstringTwoDistinct
        >>> fn("")
        0
        >>> fn("eceba")
        3
        >>> fn("ccaabbb")
        5
        """
        left, res, idxs = 0, 0, {}
        for i, c in enumerate(s):
            idxs[c] = i
            if len(idxs) == 3:
                left = idxs.pop(s[min(idxs.values())]) + 1
            res = max(res, i - left + 1)
        return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
