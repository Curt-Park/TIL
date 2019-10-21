"""
https://leetcode.com/problems/4sum/

18. 4Sum
Medium

Given an array nums of n integers and an integer target,
are there elements a, b, c, and d in nums such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.

Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

from itertools import combinations, product


class Solution:
    def fourSum3(self, nums: List[int], target: int) -> List[List[int]]:
        """O(N^3) / O(1)"""
        ret, i = [], 0
        nums.sort()
        while i < len(nums) - 1:
            old_i, j = i, len(nums) - 1
            while i < j:
                old_j, l, r = j, i + 1, j - 1
                while l < r:
                    a, b, c, d = nums[i], nums[j], nums[l], nums[r]
                    val, old_l, old_r = a + b + c + d, l, r
                    if val == target:
                        ret.append([a, b, c, d])
                        while l < r and nums[old_l] == nums[l]: l += 1
                        while l < r and nums[old_r] == nums[r]: r -= 1
                    elif val < target: l += 1
                    else: r -= 1
                while i < j and nums[old_j] == nums[j]: j -= 1
            while i < len(nums) - 1 and nums[old_i] == nums[i]: i += 1
        return ret

    def fourSum2(self, nums: List[int], target: int) -> List[List[int]]:
        """Faster than 3rd solution: O(N^4) / O(N^2) in the worst case (all 0)."""
        dic, ret = {}, set()
        for i, j in combinations(range(len(nums)), 2):
            dic.setdefault(nums[i] + nums[j], []).append((i, j))
        for k in dic:
            for t1, t2 in product(dic[k], dic.get(target - k, [])):
                if all(idx not in t2 for idx in t1):
                    ret.add(tuple(sorted(nums[idx] for idx in t1 + t2)))
        return [list(e) for e in ret]

    def fourSum1(self, nums: List[int], target: int) -> List[List[int]]:
        """Time over!: O(N^4) / O(1)"""
        ret = set()
        for idxs in combinations(range(len(nums)), 4):
            if sum(nums[i] for i in idxs) == target:
                ret.add(tuple(sorted(nums[i] for i in idxs)))
        return [list(e) for e in ret]
