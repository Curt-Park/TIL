"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

3. Longest Substring Without Repeating Characters
Medium

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """O(N) / O(N)"""
        ans, substr, check = 0, deque(), set()
        for ch in s:
            while ch in check:
                check.remove(substr.popleft())
            substr.append(ch)
            check.add(ch)
            ans = max(ans, len(substr))
        return ans
