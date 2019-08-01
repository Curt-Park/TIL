"""
https://leetcode.com/problems/subarray-sum-equals-k/
560. Subarray Sum Equals K
Medium


Given an array of integers and an integer k,
you need to find the total number of continuous subarrays
whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
Note:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and
the range of the integer k is [-1e7, 1e7].
"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """ O(N), O(N)
        >>> fn = Solution().subarraySum
        >>> fn([1], 1)
        1
        >>> fn([1,1,1], 2)
        2
        >>> fn([1,1,1], 1)
        3
        >>> fn([1,1,1,1,1], 3)
        3
        >>> fn([1,1,-1,1,1], 3)
        1
        >>> fn([1,1,-1,1,1], 2)
        4
        >>> fn([-1,-1,1,-1,-1], -2)
        4
        >>> fn([5,4,3,4,5], 9)
        2
        >>> fn([5,2,3,2,5], 5)
        4
        >>> fn([0,0,1,0,0], 1)
        9
        >>> fn([1,2,3,4,5], 6)
        1
        """
        tot, cnt, dic = 0, 0, {0: 1}
        for n in nums:
            tot += n
            if tot - k in dic:
                cnt += dic[tot - k]
            dic[tot] = dic[tot] + 1 if tot in dic else 1
        return cnt


if __name__ == "__main__":
    import doctest
    doctest.testmod()
