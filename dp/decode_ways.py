"""
https://leetcode.com/problems/decode-ways/

91. Decode Ways
Medium

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

226
2: 1
22: 2
226: 3
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        """O(N) / O(1)"""
        two, a, b, c = 0, 1, 1, 0
        for ch in s:
            one = int(ch)
            two = two % 10 * 10 + one
            c += b if 1 <= one <= 9 else 0
            c += a if 10 <= two <= 26 else 0
            a, b, c = b, c, 0
        return b
