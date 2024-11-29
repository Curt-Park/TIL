#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    # O(N) / O(N)
    def productExceptSelf_0(self, nums: List[int]) -> List[int]:
        prefix, suffix = [], []
        # prefix
        prod = 1
        for n in nums:
            prod *= n
            prefix.append(prod)
        # suffix
        prod = 1
        for n in reversed(nums):
            prod *= n
            suffix.append(prod)
        suffix = suffix[::-1]

        ans = []
        for i in range(len(nums)):
            pre = prefix[i - 1] if i - 1 >= 0 else 1
            suf = suffix[i + 1] if i + 1 < len(nums) else 1
            ans.append(pre * suf)
        return ans

    # O(N) / O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod, suffix_prod = 1, 1
        ans = []
        for n in nums:
            ans.append(prefix_prod)
            prefix_prod *= n
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= suffix_prod
            suffix_prod *= nums[i]
        return ans
        
# @lc code=end

