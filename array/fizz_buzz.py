"""
https://leetcode.com/problems/fizz-buzz/

412. Fizz Buzz
Easy

975

1315

Add to List

Share
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""


class Solution:
    def fizzBuzz2(self, n: int) -> List[str]:
        """O(N) / O(1)"""
        return [
            (i % 3 == 0) * "Fizz" + (i % 5 == 0) * "Buzz" or str(i) for i in range(1, n+1)
        ]

    def fizzBuzz1(self, n: int) -> List[str]:
        """O(N) / O(1)"""
        sol = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                sol.append("FizzBuzz")
            elif i % 5 == 0:
                sol.append("Buzz")
            elif i % 3 == 0:
                sol.append("Fizz")
            else:
                sol.append(str(i))
        return sol
