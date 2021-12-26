"""
Numbers With Same Consecutive Differences

Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.



Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]


Note:

1 <= N <= 9
0 <= K <= 9
"""


class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        """O(2^N) / O(N)"""
        def backtrack(s: str, n: int, sol: List[int]):
            if n == 0:
                sol += (len(s) == 1 or s[0] != "0") * [int(s)]
                return
            last_num = int(s[-1])
            if 0 <= last_num - K <= 9:
                backtrack(s + str(last_num - K), n-1, sol)
            if K != 0 and 0 <= last_num + K <= 9:
                backtrack(s + str(last_num + K), n-1, sol)
        sol = []
        for i in range(10):
            backtrack(str(i), N-1, sol)
        return sol
