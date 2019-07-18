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
    def multiply2(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        >>> fn = Solution().multiply2
        >>> fn('0', '123')
        '0'
        >>> fn('2', '3')
        '6'
        >>> fn('123', '456')
        '56088'
        """
        if num1 == '0' or num2 == '0':
            return '0'

        n1, n2, val = len(num1), len(num2), 0
        num1, num2 = num1[::-1], num2

        for i in range(n2):
            carry = 0
            val *= 10
            for j in range(n1):
                val1 = ord(num1[j])-ord('0')
                val2 = ord(num2[i])-ord('0')
                mul = val1 * val2 + carry
                val += mul % 10
                carry += mul // 10
            if carry > 0:
                val += carry * 10**n1

        return str(val)

    def multiply1(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        >>> fn = Solution().multiply1
        >>> fn('0', '123')
        '0'
        >>> fn('2', '3')
        '6'
        >>> fn('123', '456')
        '56088'
        """
        def strToInt(num, n):
            ret = 0
            for i in range(n):
                ret += (ord(num[n-i-1]) - ord('0')) * 10**i
            return ret

        def IntToStr(num, n):
            ret = []
            for i in reversed(range(n)):
                digit = num // 10**i
                if ret or digit != 0:
                    ret.append(str(digit))
                num %= 10**i
            return "".join(ret)

        if num1 == "0" or num2 == "0":
            return "0"

        n1, n2 = len(num1), len(num2)
        num1, num2 = strToInt(num1, n1), strToInt(num2, n2)
        return IntToStr(num1 * num2, n1 + n2)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
