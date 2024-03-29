"""2044. Count Number of Maximum Bitwise-OR Subsets

https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

Medium


Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.

The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).

Example 1:
Input: nums = [3,1]
Output: 2
Explanation: The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
- [3]
- [3,1]

Example 2:
Input: nums = [2,2,2]
Output: 7
Explanation: All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 23 - 1 = 7 total subsets.

Example 3:

Input: nums = [3,2,1,5]
Output: 6
Explanation: The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:
- [3,5]
- [3,1,5]
- [3,2,5]
- [3,2,1,5]
- [2,5]
- [2,1,5]


Constraints:
1 <= nums.length <= 16
1 <= nums[i] <= 105
"""


class Solution:
    def countMaxOrSubsets2(self, nums: List[int]) -> int:
        """O(N^2) / O(N^2)."""
        dp = {0: 1}
        for n in nums:
            for bitwise_or, cnt in list(dp.items()):
                bitwise_or |= n
                dp.setdefault(bitwise_or, 0)
                dp[bitwise_or] += cnt
        return dp[max(dp)]

    def countMaxOrSubsets1(self, nums: List[int]) -> int:
        """O(2^N) / O(2^N)."""
        counter = {}
        for n in range(1, len(nums) + 1):
            for subset in itertools.combinations(nums, n):
                bitwise_or = functools.reduce(lambda x, y: x | y, subset)
                counter.setdefault(bitwise_or, 0)
                counter[bitwise_or] += 1
        return counter[max(counter)]

    def countMaxOrSubsets0(self, nums: List[int]) -> int:
        """O(2^N) / O(N)."""
        max_bitwise_or = self.bitwise_or(nums)
        return sum(
            max_bitwise_or == self.bitwise_or(subset)
            for n in range(1, len(nums) + 1)
            for subset in itertools.combinations(nums, n)
        )

    def bitwise_or(self, nums: List[int]) -> int:
        return functools.reduce(lambda x, y: x | y, nums)
