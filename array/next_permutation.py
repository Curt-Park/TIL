"""
https://leetcode.com/problems/next-permutation/
Next Permutation
Medium

Implement next permutation, which rearranges numbers into the lexicographically
next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest
possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and
its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        >>> fn = Solution().nextPermutation
        >>> fn([1, 2, 3])
        [1, 3, 2]
        >>> fn([3, 2, 1])
        [1, 2, 3]
        >>> fn([1, 1, 5])
        [1, 5, 1]
        """
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
