"""
Plus One
Medium
https://leetcode.com/problems/plus-one/

Given a non-empty array of digits representing a non-negative integer,
plus one to the integer.
The digits are stored such that the most significant digit is
at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero,
except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""


class Solution(object):
    def plusOne(self, digits):
        """ O(N), O(N)
        :type digits: List[int]
        :rtype: List[int]
        >>> fn = Solution().plusOne
        >>> fn([0])
        [1]
        >>> fn([9,9])
        [1, 0, 0]
        >>> fn([1,2,3])
        [1, 2, 4]
        >>> fn([4,3,2,1])
        [4, 3, 2, 2]
        """
        digits, carry = digits[::-1], 1
        for i in range(len(digits)):
            carry, digits[i] = divmod(digits[i] + carry, 10)
        if carry != 0:
            digits.append(carry)
        return digits[::-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
