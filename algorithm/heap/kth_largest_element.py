"""
https://leetcode.com/problems/kth-largest-element-in-an-array/

215. Kth Largest Element in an Array
Medium

Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order,
not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

import heapq
from typing import List


class Solution:
    def findKthLargest3(self, nums: List[int], k: int) -> int:
        """ Avg O(N), O(1)
        >>> fn = Solution().findKthLargest3
        >>> fn([3,2,1,5,6,4], 2)
        5
        >>> fn([3,2,3,1,2,4,5,5,6], 4)
        4
        """
        def partition(left, right):
            piv = right
            for k in range(left, right + 1):
                if nums[piv] <= nums[k]:
                    nums[left], nums[k] = nums[k], nums[left]
                    left += 1
            return left - 1

        left, right, k = 0, len(nums) - 1, k - 1
        while True:
            pos = partition(left, right)
            if pos == k:
                return nums[pos]
            elif pos > k:
                right = pos - 1
            elif pos < k:
                left = pos + 1

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        """ Avg O(N), O(K)
        >>> fn = Solution().findKthLargest2
        >>> fn([3,2,1,5,6,4], 2)
        5
        >>> fn([3,2,3,1,2,4,5,5,6], 4)
        4
        """
        def quickSelect(nums, i, j, k) -> List[int]:
            piv, left, right = i, i + 1, j
            while left <= right:
                while left <= right and nums[piv] < nums[left]:
                    left += 1
                while left <= right and nums[right] <= nums[piv]:
                    right -= 1
                if left <= right:
                    nums[left], nums[right] = nums[right], nums[left]
            nums[piv], nums[right] = nums[right], nums[piv]
            if right == k:
                return nums[k]
            elif right < k:
                return quickSelect(nums, left, j, k)
            elif right > k:
                return quickSelect(nums, i, right, k)
        return quickSelect(nums, 0, len(nums) - 1, k - 1)

    def findKthLargest1(self, nums: List[int], k: int) -> int:
        """ O(NlogK), O(K)
        >>> fn = Solution().findKthLargest1
        >>> fn([3,2,1,5,6,4], 2)
        5
        >>> fn([3,2,3,1,2,4,5,5,6], 4)
        4
        """
        heap = []
        for num in nums:
            if len(heap) == k:
                heapq.heappushpop(heap, num)
            else:
                heapq.heappush(heap, num)
        return heap[0]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
