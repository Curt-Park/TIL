"""
https://leetcode.com/problems/split-array-largest-sum/

410. Split Array Largest Sum
Hard

Given an array which consists of non-negative integers and an integer m,
you can split the array into m non-empty continuous subarrays.
Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)

Examples:
Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """O(Nlog(sumOfArr - maxVal)) / O(1)"""
        def split(max_sum: int) -> int:
            pieces, tmp_sum = 1, 0
            for num in nums:
                next_sum = tmp_sum + num
                if next_sum > max_sum: tmp_sum, pieces = num, pieces + 1
                else: tmp_sum = next_num
            return pieces

        l, r = max(nums), sum(nums)
        while l <= r:
            mid = (l + r) // 2
            pieces = split(mid)
            if pieces > m: l = mid + 1
            else: r = mid - 1
        return l
