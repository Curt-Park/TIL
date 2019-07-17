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
    def nextPermutation2(self, nums):
        """ O(N), O(1)
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        >>> fn = Solution().nextPermutation2
        >>> fn([1, 2, 3])
        [1, 3, 2]
        >>> fn([3, 2, 1])
        [1, 2, 3]
        >>> fn([1, 1, 5])
        [1, 5, 1]
        >>> fn([5, 4, 2, 3, 1])
        [5, 4, 3, 1, 2]
        >>> fn([5, 4, 2, 9, 9])
        [5, 4, 9, 2, 9]
        >>> fn([5, 4, 2, 9, 5, 4])
        [5, 4, 4, 2, 5, 9]
        """
        asc, n = -1, len(nums)
        for i in range(n-1):
            if nums[i] < nums[i+1]:
                asc = i
        next_min = asc + 1
        for i in range(asc+2, n):
            if nums[asc] < nums[i] <= nums[next_min]:
                next_min = i
        if asc != -1:
            nums[asc], nums[next_min] = nums[next_min], nums[asc]
        start, end = asc + 1, n - 1
        for i in range((end - start) // 2 + 1):
            nums[start+i], nums[end-i] = nums[end-i], nums[start+i]

        return nums

    def nextPermutation1(self, nums):
        """ O(NlogN), O(N)
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        >>> fn = Solution().nextPermutation1
        >>> fn([1, 2, 3])
        [1, 3, 2]
        >>> fn([3, 2, 1])
        [1, 2, 3]
        >>> fn([1, 1, 5])
        [1, 5, 1]
        >>> fn([5, 4, 2, 3, 1])
        [5, 4, 3, 1, 2]
        >>> fn([5, 4, 2, 9, 9])
        [5, 4, 9, 2, 9]
        >>> fn([5, 4, 2, 9, 5, 4])
        [5, 4, 4, 2, 5, 9]
        """
        n = len(nums)
        asc = -1
        for i in range(n-1):
            if nums[i] < nums[i+1]:
                asc = i
        next_min = asc + 1
        for i in range(asc+2, n):
            if nums[asc] < nums[i] <= nums[next_min]:
                next_min = i
        nums[asc], nums[next_min] = nums[next_min], nums[asc]
        nums[asc+1:] = sorted(nums[asc+1:])

        return nums


if __name__ == "__main__":
    import doctest
    doctest.testmod()
