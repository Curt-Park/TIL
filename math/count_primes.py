"""
https://leetcode.com/problems/count-primes/


204. Count Primes
Easy

Count the number of prime numbers less than a non-negative number, n.

Example:
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""


class Solution:
    # Sieve of Eratosthenes
    def countPrimes2(self, n: int) -> int:
        """O(logNloglogN) / O(N)"""
        primes = [False] * 2 + [True] * (n - 2)
        for i in range(2, int(n**0.5) + 1):
            if not primes[i]: continue
            for j in range(i**2, n, i):
                primes[j] = False
        return sum(primes)
        
    def countPrimes1(self, n: int) -> int:
        """O(NlogN) / O(1)"""
        def isPrime(n: int) -> bool:
            if n <= 1: return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0: return False
            return True
        return sum(isPrime(i) for i in range(n))
        
        
if __name__ == "__main__":
    fn1 = Solution().countPrimes1
    fn2 = Solution().countPrimes2
    assert fn1(0) == fn2(0)
    assert fn1(1) == fn2(1)
    assert fn1(10) == fn2(10)
    assert fn1(100) == fn2(100)
