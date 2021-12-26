"""
https://leetcode.com/problems/add-two-numbers/description/
Add Two Numbers
Medium

You are given two nonempty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes
contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

from typing import List


class Solution:
    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur_l, cur_r, add = l1, l2, 0
        cur = ret = ListNode(0)
        while cur_l or cur_r or add:
            if cur_l:
                add, cur_l = add + cur_l.val, cur_l.next
            if cur_r:
                add, cur_r = add + cur_r.val, cur_r.next
            add, val = divmod(add, 10)
            cur = cur.next = ListNode(val)
        return ret.next

