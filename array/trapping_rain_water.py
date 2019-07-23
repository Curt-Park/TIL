"""
https://leetcode.com/problems/trapping-rain-water/

42. Trapping Rain Water
Hard
Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it is able to trap after raining.

https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


class Solution(object):
    def trap3(self, height):
        """ O(N), O(1)
        :type height: List[int]
        :rtype: int
        >>> fn = Solution().trap3
        >>> fn([0,2,1,0])
        0
        >>> fn([0,1,0,2])
        1
        >>> fn([2,1,1,2])
        2
        >>> fn([5,4,1,2])
        1
        >>> fn([2,0,1,1,1,1])
        1
        >>> fn([2,0,1,1,2,1])
        4
        >>> fn([2,0,0,1,2,1])
        5
        >>> fn([3,2,2,1,2,3])
        5
        >>> fn([1,1,0,1,1,2,1])
        1
        >>> fn([0,1,0,2,1,0,1,3])
        5
        >>> fn([5,4,3,2,1,0,5])
        15
        >>> fn([0,5,1,2,3,4,5])
        10
        >>> fn([0,5,0,2,1,0,1,0,5])
        26
        >>> fn([0,1,0,2,1,0,1,3,2,1,2,1])
        6
        """
        n, water = len(height), 0
        left, right, left_max, right_max = 0, n - 1, 0, 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]p
                right -= 1
        return water

    def trap2(self, height):
        """ O(N), O(N)
        :type height: List[int]
        :rtype: int
        >>> fn = Solution().trap2
        >>> fn([0,2,1,0])
        0
        >>> fn([0,1,0,2])
        1
        >>> fn([2,1,1,2])
        2
        >>> fn([5,4,1,2])
        1
        >>> fn([2,0,1,1,1,1])
        1
        >>> fn([2,0,1,1,2,1])
        4
        >>> fn([2,0,0,1,2,1])
        5
        >>> fn([3,2,2,1,2,3])
        5
        >>> fn([1,1,0,1,1,2,1])
        1
        >>> fn([0,1,0,2,1,0,1,3])
        5
        >>> fn([5,4,3,2,1,0,5])
        15
        >>> fn([0,5,1,2,3,4,5])
        10
        >>> fn([0,5,0,2,1,0,1,0,5])
        26
        >>> fn([0,1,0,2,1,0,1,3,2,1,2,1])
        6
        """
        n, water, stack = len(height), 0, []
        for i in range(n):
            while stack and height[stack[-1]] < height[i]:
                mid = stack.pop()
                if not stack:
                    break
                left, right = stack[-1], i
                h = min(height[left], height[right]) - height[mid]
                w = right - left - 1
                water += w * h
            stack.append(i)
        return water

    def trap1(self, height):
        """ O(N^2), O(N)
        :type height: List[int]
        :rtype: int
        >>> fn = Solution().trap1
        >>> fn([0,2,1,0])
        0
        >>> fn([0,1,0,2])
        1
        >>> fn([2,1,1,2])
        2
        >>> fn([5,4,1,2])
        1
        >>> fn([2,0,1,1,1,1])
        1
        >>> fn([2,0,1,1,2,1])
        4
        >>> fn([2,0,0,1,2,1])
        5
        >>> fn([3,2,2,1,2,3])
        5
        >>> fn([1,1,0,1,1,2,1])
        1
        >>> fn([0,1,0,2,1,0,1,3])
        5
        >>> fn([5,4,3,2,1,0,5])
        15
        >>> fn([0,5,1,2,3,4,5])
        10
        >>> fn([0,5,0,2,1,0,1,0,5])
        26
        >>> fn([0,1,0,2,1,0,1,3,2,1,2,1])
        6
        """
        n, cnt, stack = len(height), 0, []
        for i in range(1, n):
            if height[i - 1] > height[i]:
                if not stack or height[stack[-1]] < height[i - 1]:
                    stack.append(i - 1)
            elif height[i - 1] < height[i] and stack:
                left, right = stack[-1], i
                h = min(height[left], height[right])
                if height[left] == h:
                    stack.pop()
                for j in range(left+1, right):
                    if height[j] < h:
                        cnt += (h - height[j])
                        height[j] = h
        return cnt


if __name__ == "__main__":
    import doctest
    doctest.testmod()
