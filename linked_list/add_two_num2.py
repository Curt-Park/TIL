"""
https://leetcode.com/problems/add-two-numbers-ii/

445. Add Two Numbers II
Medium

You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

from collections import defaultdict


class Solution:
    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """O(max(M, N)) / O(1)"""
        p1, p2, n1, n2 = l1, l2, 0, 0
        while p1 or p2:
            if p1: n1, p1 = n1 * 10 + p1.val, p1.next
            if p2: n2, p2 = n2 * 10 + p2.val, p2.next
        s, prev = n1 + n2, None
        while s:
            node = ListNode(s % 10)
            prev, node.next, s = node, prev, s // 10
        return [prev, ListNode(0)][prev is None]

    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """O(M+N) / O(max(M, N))"""
        def iterate(l: ListNode) -> int:
            if l is None: return 0
            idx = iterate(l.next) + 1
            d[idx] += l.val
            return idx
        d, prev = defaultdict(lambda: 0), None
        for i in range(max(iterate(l1), iterate(l2)) + 1):
            d[i+2] += d[i+1] // 10
            node = ListNode(d[i+1] % 10)
            prev, node.next = node, prev
        return [prev, prev.next][prev.val == 0]
