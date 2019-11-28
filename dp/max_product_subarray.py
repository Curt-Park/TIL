"""
https://leetcode.com/problems/maximum-product-subarray/

152. Maximum Product Subarray
Medium

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """O(N) / O(1)"""
        dp0, dp1, ans = 0, 0, nums[0]
        for i in range(len(nums)):
            dp0 = dp0 * nums[i] or nums[i]
            dp1 = dp1 * nums[-i - 1] or nums[-i - 1]
            ans = max(ans, dp0, dp1)
        return ans
