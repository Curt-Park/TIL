"""
189. Rotate Array
Medium

Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?


Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:
1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """O(N) / O(1)"""
        cur_idx, start, cnt, k = -1, -1, 0, k % len(nums)
        while cnt < len(nums):
            if cur_idx == start:
                start += 1
                tmp, cur_idx = nums[start], start
            next_idx = (cur_idx + k) % len(nums)
            tmp, nums[next_idx] = nums[next_idx], tmp
            cnt, cur_idx = cnt + 1, next_idx

    def rotate(self, nums: List[int], k: int) -> None:
        """O(N) / O(N)"""
        nums[:] = nums[-k % len(nums):] + nums[:-k % len(nums)]

    def rotate(self, nums: List[int], k: int) -> None:
        """O(N) / O(N)"""
        for i, n in enumerate(nums[-k % len(nums):] + nums[:-k % len(nums)]):
            nums[i] = n
