"""
https://leetcode.com/problems/happy-number/

202. Happy Number
Easy

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the
sum of the squares of its digits, and repeat the process until
the number equals 1 (where it will stay), or it loops endlessly
in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true

Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


class Solution:
    def isHappy3(self, n: int) -> bool:
        """O(?), O(1)"""
        step = lambda n: sum(int(x)**2 for x in str(n))
        return n == 1 or n > 4 and self.isHappy3(step(n))
    
    def isHappy2(self, n: int) -> bool:
        """O(?), O(1)"""
        step = lambda n: sum(int(x)**2 for x in str(n))
        s, f = n, step(n)
        while s != f:
            s, f = step(s), step(step(f))
        return s == 1
        
    def isHappy1(self, n: int) -> bool:
        """O(?), O(?)"""
        seen = {1}
        while n not in seen:
            seen.add(n)
            n = sum(int(x)**2 for x in str(n))
        return n == 1
        
    def isHappy0(self, n: int) -> int:
        """Test."""
        seen, i = {1}, 0
        while n not in seen:
            seen.add(n)
            n = sum(int(x)**2 for x in str(n))
            i += 1
        return i
        

if __name__ == "__main__":
    fn = Solution().isHappy0
    max_iter = 0
    for i in range(1, 2**31):
        iter_n = fn(i)
        if max_iter < iter_n:
            max_iter = iter_n
            print(i, iter_n)
    print("max_iter", max_iter)
