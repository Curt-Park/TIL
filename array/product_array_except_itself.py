"""
https://leetcode.com/problems/product-of-array-except-self/

238. Product of Array Except Self
Medium

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""


class Solution:
    def productExceptSelf3(self, nums: List[int]) -> List[int]:
        """O(N) / O(1): One-pass"""
        ret, n, l_mul, r_mul = [1] * len(nums), len(nums), 1, 1
        for i in range(n - 1):
            l_mul *= nums[i]
            r_mul *= nums[n - i - 1]
            ret[i + 1] *= l_mul
            ret[n - i - 2] *= r_mul
        return ret

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        """O(N) / O(1)"""
        ret, l_mul, r_mul = [1] * len(nums), 1, 1
        for i in range(len(nums) - 1):
            l_mul *= nums[i]
            ret[i + 1] *= l_mul
        for i in reversed(range(1, len(nums))):
            r_mul *= nums[i]
            ret[i - 1] *= r_mul
        return ret

    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        """O(N) / O(N)"""
        l_prod, r_prod = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            l_prod[i] = l_prod[i - 1] * nums[i - 1]
        for i in reversed(range(len(nums) - 1)):
            r_prod[i] = r_prod[i + 1] * nums[i + 1]
        return [l_prod[i] * r_prod[i] for i in range(len(nums))]
