"""
https://leetcode.com/problems/iterator-for-combination/

1286. Iterator for Combination
Medium

Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.


Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false


Constraints:

1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It's guaranteed that all calls of the function next are valid.
"""

from itertools import combinations


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self._combs = combinations(characters, combinationLength)
        self._next = next(self._combs, None)

    def next(self) -> str:
        ret = "".join(self._next) if self._next else None
        self._next = next(self._combs, None)
        return ret

    def hasNext(self) -> bool:
        return self._next is not None
