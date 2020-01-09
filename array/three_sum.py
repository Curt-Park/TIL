"""
https://leetcode.com/problems/3sum/

15. 3Sum
Medium

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

from collections import defaultdict
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """O(N^2) / O(1)"""
        N, ans = len(nums), []
        nums.sort()
        for i in range(N - 2):
            if i and nums[i - 1] == nums[i]:
                continue
            j, k = i + 1, N - 1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum:
                    j, k = j + (three_sum < 0), k - (three_sum > 0)
                    continue
                ans.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                while j < k and nums[k - 1] == nums[k]:
                    k -= 1
                j, k = j + 1, k - 1
        return ans

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        >>> threeSum = Solution().threeSum
        >>> threeSum([-1, 0, 1, 2, -1, -4])
        [[-1, -1, 2], [-1, 0, 1]]
        >>> threeSum([-2, -1, 0, 1, 2, -1, -4])
        [[-2, 0, 2], [-1, -1, 2], [-1, 0, 1]]
        >>> threeSum([-1, -1, -1, 0, 1, 1, 1])
        [[-1, 0, 1]]
        >>> threeSum([-2, -1, -1, -1, 0, 1, 1, 1])
        [[-2, 1, 1], [-1, 0, 1]]
        >>> threeSum([0,0,0,0,0])
        [[0, 0, 0]]
        >>> threeSum([-1, -1, -1, 1, 1, 1])
        []
        >>> threeSum([-1, 0])
        []
        >>> threeSum([0])
        []
        >>> threeSum([])
        []
        """
        n = len(nums)
        nums.sort()
        ret = []

        for i in range(n-2):
            # because all elements are sorted,
            # we don't have to look more if the current element is bigger than 0
            if nums[i] > 0:
                break

            # If the number is the same as the number before,
            # we have used it as target already, continue.
            if i > 0 and nums[i-1] == nums[i]:
                continue

            l = i + 1
            r = n - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    ret.append([nums[i], nums[l], nums[r]])
                    while l < n - 1 and nums[l] == nums[l+1]:
                        l += 1
                    while r > i + 1 and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1

        return ret

    def failedThreeSum(self, nums: List[int]) -> List[List[int]]:
        """
        311 / 313 passes...

        >>> threeSum = Solution().failedThreeSum
        >>> threeSum([-1, 0, 1, 2, -1, -4])
        [[-1, 0, 1], [-1, -1, 2]]
        >>> threeSum([-1, -1, -1, 0, 1, 1, 1])
        [[-1, 0, 1]]
        >>> threeSum([0,0,0,0,0])
        [[0, 0, 0]]
        >>> threeSum([-1, -1, -1, 1, 1, 1])
        []
        >>> threeSum([-1, 0])
        []
        >>> threeSum([0])
        []
        >>> threeSum([])
        []
        """
        cnt = defaultdict(lambda: 0)
        pairs= set()
        n = len(nums)

        #  nlogn
        nums.sort()

        #  n^2
        for i in range(n):
            cnt[nums[i]] += 1
            for j in range(i+1, n):
                pairs.add((nums[i], nums[j]))

        #  n^2
        ret = []
        triples = set()
        for v1, v2 in pairs:
            v3 = -(v1 + v2)
            cnt[v1] -= 1; cnt[v2] -= 1

            if 0 < cnt[v3]:
                if v2 <= v3:
                    triplet = (v1, v2, v3)
                elif v3 <= v1:
                    triplet = (v3, v1, v2)
                else:
                    triplet = (v1, v3, v2)

                if not triplet in triples:
                    ret.append(list(triplet))
                    triples.add(triplet)

            cnt[v1] += 1; cnt[v2] += 1

        return ret

    def bruteForce(self, nums: List[int]) -> List[List[int]]:
        """
        >>> s = Solution()
        >>> s.bruteForce([-1, 0, 1, 2, -1, -4])
        [[-1, 0, 1], [-1, -1, 2]]
        >>> s.bruteForce([-1, -1, -1, 0, 1, 1, 1])
        [[-1, 0, 1]]
        >>> s.bruteForce([0,0,0,0,0])
        [[0, 0, 0]]
        >>> s.bruteForce([-1, -1, -1, 1, 1, 1])
        []
        >>> s.bruteForce([-1, 0])
        []
        >>> s.bruteForce([0])
        []
        >>> s.bruteForce([])
        []
        """
        n = len(nums)
        ret = []

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    triplet = sorted([nums[i], nums[j], nums[k]])
                    if sum(triplet) == 0 and not triplet in ret:
                        ret.append(triplet)

        return ret


if __name__ == "__main__":
    import doctest
    doctest.testmod()
