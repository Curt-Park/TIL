"""
https://leetcode.com/problems/asteroid-collision/

735. Asteroid Collision
Medium

We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.


Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
Example 4:

Input: asteroids = [-2,-1,1,2]
Output: [-2,-1,1,2]
Explanation: The -2 and -1 are moving left, while the 1 and 2 are moving right. Asteroids moving the same direction never meet, so no asteroids will meet each other.


Constraints:

1 <= asteroids <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """O(N) / O(N)"""
        stack = list()
        for ast in asteroids:
            stack.append(ast)
            while len(stack) >= 2:
                r, l = stack.pop(), stack.pop()
                if r < 0 and 0 < l:
                    stack += (l > -r) * [l] or (l < -r) * [r]
                else:
                    stack += [l, r]
                    break
        return stack
