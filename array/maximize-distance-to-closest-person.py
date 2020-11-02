"""
https://leetcode.com/problems/maximize-distance-to-closest-person/

849. Maximize Distance to Closest Person
Medium

You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.
Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.
Return that maximum distance to the closest person.

Example 1:

Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation:
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: seats = [1,0,0,0]
Output: 3
Explanation:
If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Example 3:

Input: seats = [0,1]
Output: 1


Constraints:

2 <= seats.length <= 2 * 104
seats[i] is 0 or 1.
At least one seat is empty.
At least one seat is occupied.
"""


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        """O(N) / O(1)"""
        last, max_dist = None, 0
        for i, occ in enumerate(seats):
            if not occ:
                continue
            dist = i if last is None else (i - last) // 2
            max_dist = max(max_dist, dist)
            last = i
        return max(max_dist, len(seats) - last - 1)

    def maxDistToClosest(self, seats: List[int]) -> int:
        """O(N!) / O(1)"""
        max_dist = 0
        for i, occ in enumerate(seats):
            if occ:
                continue
            l, r, dist = i, i, 0
            while 0 <= l or r < len(seats):
                if seats[l] or seats[r]:
                    break
                dist += 1
                l -= (l > 0)
                r += (r < len(seats) - 1)
            max_dist = max(max_dist, dist)
        return max_dist
