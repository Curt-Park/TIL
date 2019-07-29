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

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        >>> fn = Solution().findKthLargest
        >>> fn([3,2,1,5,6,4], 2)
        5
        >>> fn([3,2,3,1,2,4,5,5,6], 4)
        4
        """
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
