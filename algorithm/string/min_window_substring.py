"""
https://leetcode.com/problems/minimum-window-substring/
Minimum Window Substring
Hard

Given a string S and a string T, find the minimum window in S which will
contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:
If there is no such window in S that covers all characters in T,
return the empty string "".
If there is such window, you are guaranteed that there will always
be only one unique minimum window in S.
"""


from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """ O(N), O(M)
        :type s: str
        :type t: str
        :rtype: str
        >>> fn = Solution().minWindow
        >>> fn("ADOBECODEBANC", "ABC")
        'BANC'
        >>> fn("ABBBBEEODEBAC", "ABC")
        'BAC'
        >>> fn("ABBBBEEODEBAC", "ABB")
        'ABB'
        >>> fn("AAAABEEODEBAC", "ABB")
        'ABEEODEB'
        >>> fn("AA", "AA")
        'AA'
        >>> fn("ABBBBEEODEBAC", "ABCZ")
        ''
        >>> fn("", "ABCZ")
        ''
        >>> fn("ABBBBEEODEBAC", "")
        ''
        """
        need, missing = Counter(t), len(t)
        left = w_l = w_r = 0
        for right, ch in enumerate(s, 1):
            missing -= need[ch] > 0
            need[ch] -= 1
            if not missing:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                if not w_r or right - left < w_r - w_l:
                    w_l, w_r = left, right
        return s[w_l:w_r]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
