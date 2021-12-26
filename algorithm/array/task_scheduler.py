"""
https://leetcode.com/problems/task-scheduler/
621. Task Scheduler
Medium

Given a char array representing tasks CPU need to do.
It contains capital letters A to Z where different letters represent different
tasks. Tasks could be done without original order. Each task could be done
in one interval. For each interval, CPU could finish one task or just be idle.
However, there is a non-negative cooling interval n that means between
two same tasks, there must be at least n intervals that CPU are doing
different tasks or just be idle.
You need to return the least number of intervals the CPU will take
to finish all the given tasks.

Example:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.


Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""


from collections import Counter
from queue import PriorityQueue


class Solution(object):
    def leastInterval(self, tasks, n):
        """ O(N), O(1)
        :type tasks: List[str]
        :type n: int
        :rtype: int
        >>> fn = Solution().leastInterval
        >>> fn(["A","A"], 1)
        3
        >>> fn(["A","A","B"], 1)
        3
        >>> fn(["C","A","B","A"], 1)
        4
        >>> fn(["B","C","A","B","A"], 2)
        5
        >>> fn(["A","A"], 3)
        5
        >>> fn(["A","A","A","B","B","B"], 2)
        8
        >>> fn(["A","A","A","B","B","B"], 3)
        10

        Examples:
            AxxAxxA
            ABxABxAB
            8

            AxA
            ABA
            3

            AxxA
            ABxAB
            ABCAB
            5

            AxxxAxxxA
            ABxxABxxAB
            10
        """
        pq, ret = PriorityQueue(), 0
        for c in Counter(tasks).values():
            pq.put(-c)
        while not pq.empty():
            tmp, cnt = [], 0
            for _ in range(n + 1):
                if pq.empty():
                    break
                c = pq.get()
                cnt += 1
                if c < -1:
                    tmp.append(c + 1)
            for c in tmp:
                pq.put(c)
            ret += n + 1 if not pq.empty() else cnt
        return ret


if __name__ == "__main__":
    import doctest
    doctest.testmod()
