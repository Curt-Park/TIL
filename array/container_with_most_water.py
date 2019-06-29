"""

level: medium
    
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        >>> s = Solution()
        >>> s.maxArea([1,8,6,2,5,4,8,3,7])
        49
        >>> s.maxArea([8,6])
        6
        >>> s.maxArea([1,8,6])
        6
        >>> s.maxArea([1,8,7,6])
        12
        >>> s.maxArea([6,8,7,6])
        18
        >>> s.maxArea([1,2,3,4,5])
        6
        >>> s.maxArea([6,8,99,99,7,6])
        99
        >>> s.maxArea([6,5,99,99,5,6])
        99
        
        Your runtime beats 15.07 % of python3 submissions
        '''
        area = lambda l, r: (r - l) * min(height[r], height[l])
        
        left, right = 0, len(height) - 1
        max_area = area(left, right)
        
        while left + 1 < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            max_area = max(max_area, area(left, right))
            
        return max_area
            
        
    def bruteForce(self, height: List[int]) -> int:
        '''
        >>> s = Solution()
        >>> s.bruteForce([1,8,6,2,5,4,8,3,7])
        49
        >>> s.bruteForce([8,6])
        6
        >>> s.bruteForce([1,8,6])
        6
        >>> s.bruteForce([1,8,7,6])
        12
        >>> s.bruteForce([6,8,7,6])
        18
        '''
        n = len(height)
        max_water = 0
        
        for i in range(n):
            for j in range(i+1, n):
                water = (j - i) * min(height[i], height[j])
                max_water = max(water, max_water)
                
        return max_water
        
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
