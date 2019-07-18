"""
https://leetcode.com/problems/jump-game/
medium

Given an array of non-negative integers, you are initially positioned
at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation:
Jump 1 step from index 0 to 1, then 3 steps to the last index.


Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation:
You will always arrive at index 3 no matter what. Its maximum
jump length is 0, which makes it impossible to reach the last index.
"""


class Solution(object):
    def canJump(self, nums):
        """ O(N^2), O(N)  => Time Limit Exceeded...  [74/75]
        :type nums: List[int]
        :rtype: bool
        >>> fn = Solution().canJump
        >>> fn([2,3,1,1,4])
        True
        >>> fn([3,2,1,0,4])
        False
        >>> fn([3,2,1,1,4])
        True
        >>> fn([0])
        True
        """
        n = len(nums)
        flags = [False] * (n - 1) + [True]

        for i in reversed(range(n - 1)):
            if sum(flags[i+1:min(i+nums[i]+1, n)]) > 0:
                flags[i] = True

        return flags[0]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
