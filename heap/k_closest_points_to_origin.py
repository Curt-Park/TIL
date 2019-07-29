"""
https://leetcode.com/problems/k-closest-points-to-origin/

973. K Closest Points to Origin
Medium

We have a list of points on the plane.  
Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.  
The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 

Note:
1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""

import heapq
from typing import List


class Solution:
    def kClosest2(self, points: List[List[int]], K: int) -> List[List[int]]:
        """ O(NlogK), O(N)
        >>> fn = Solution().kClosest2
        >>> fn([[3,3],[5,-1],[-2,4]], 2)
        [[3, 3], [-2, 4]]
        >>> fn([[1,3],[-2,2]], 1)
        [[-2, 2]]
        """
        heap = []
        dist = lambda p: p[0]**2 + p[1]**2
        for p in points:
            element = [-dist(p), p[0], p[1]]
            if len(heap) == K:
                heapq.heappushpop(heap, element)
            else:
                heapq.heappush(heap, element)
        return [e[1:] for e in heap]
        
    def kClosest1(self, points: List[List[int]], K: int) -> List[List[int]]:
        """ O(NlogN), O(N)
        >>> fn = Solution().kClosest1
        >>> fn([[3,3],[5,-1],[-2,4]], 2)
        [[3, 3], [-2, 4]]
        >>> fn([[1,3],[-2,2]], 1)
        [[-2, 2]]
        """
        def dist(point: List[int]):
            x, y = point
            return (x**2 + y**2) ** 1/2
            
        sorted_points = sorted(points, key=dist)
        return sorted_points[:K]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
