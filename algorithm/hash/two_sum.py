"""
https://leetcode.com/problems/two-sum/
1. Two Sum
Easy

Given an array of integers, return indices of the two numbers such that
they add up to a specific target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

from typing import List


class Solution:
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        """ One-pass using residual Hash: O(N), O(N)
        >>> fn = Solution().twoSum3
        >>> fn([2,7,11,15], 9)
        [0, 1]
        >>> fn([1,0,2,3,-1], 0)
        [0, 4]
        >>> fn([3,2,4], 6)
        [1, 2]
        >>> fn([3,3], 6)
        [0, 1]
        """
        residual = {}
        for i, val in enumerate(nums):
            if val in residual:
                return [residual[val], i]
            residual[target - val] = i
        return []

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        """ Using residual Hash: O(N), O(N)
        >>> fn = Solution().twoSum2
        >>> fn([2,7,11,15], 9)
        [0, 1]
        >>> fn([1,0,2,3,-1], 0)
        [0, 4]
        >>> fn([3,2,4], 6)
        [1, 2]
        >>> fn([3,3], 6)
        [0, 1]
        """
        residual = {target-val: idx for idx, val in enumerate(nums)}
        for i, key in enumerate(nums):
            if key in residual and i != residual[key]:
                return [i, residual[key]]
        return []

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        """ Using sorting and Two pointer: O(NlogN), O(N)
        >>> fn = Solution().twoSum1
        >>> fn([2,7,11,15], 9)
        [0, 1]
        >>> fn([1,0,2,3,-1], 0)
        [0, 4]
        >>> fn([3,2,4], 6)
        [1, 2]
        >>> fn([3,3], 6)
        [0, 1]
        """
        ret, left, right = [], 0, len(nums) - 1
        sorted_idx = sorted(range(len(nums)), key=lambda i: nums[i])

        while left < right:
            s = nums[sorted_idx[left]] + nums[sorted_idx[right]]
            if s == target:
                idx1 = min(sorted_idx[left], sorted_idx[right])
                idx2 = max(sorted_idx[left], sorted_idx[right])
                ret = [idx1, idx2]
                break
            elif s < target:
                left += 1
            else:
                right -= 1
        return ret


if __name__ == "__main__":
    import doctest
    doctest.testmod()
