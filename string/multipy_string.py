"""
https://leetcode.com/problems/multiply-strings/
medium

Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs
to integer directly.
"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        >>> fn = Solution().multiply
        >>> fn('0', '123')
        '0'
        >>> fn('2', '3')
        '6'
        >>> fn('123', '456')
        '56088'
        """
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
