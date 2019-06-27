"""
https://leetcode.com/explore/interview/card/google/59/array-and-strings/3047/

level: medium

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


def lengthOfLongestSubstring(s):
    '''
    >>> lengthOfLongestSubstring('abcabcbb')
    3
    >>> lengthOfLongestSubstring('abcadcbb')
    4
    >>> lengthOfLongestSubstring('bbbbb')
    1
    >>> lengthOfLongestSubstring('pwwkew')
    3
    >>> lengthOfLongestSubstring('abcde')
    5
    >>> lengthOfLongestSubstring('')
    0
    
    Your runtime beats 98.70 % of python3 submissions
    '''
    checker = {}
    start, ret = 0, 0
    
    for i, ch in enumerate(s):
        if ch in checker and start < checker[ch] + 1:
            start = checker[ch] + 1
        checker[ch] = i
        
        n = i - start + 1
        if n > ret:
            ret = n 
    
    return ret
    
if __name__ =='__main__':
    import doctest
    doctest.testmod()
