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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def printLList(head: ListNode) -> None:
    ptr = head
    if not ptr:
        print(ptr)

    while ptr:
        print(ptr.val, end="")
        if ptr.next:
            print("->", end="")
        ptr = ptr.next


def createLList(arr: List) -> ListNode:
    """
    >>> printLList(createLList([1, 2, 3, 3, 4, 4, 5]))
    1->2->3->3->4->4->5
    >>> printLList(createLList([1, 1, 1, 2, 3]))
    1->1->1->2->3
    """
    n = len(arr)

    if n == 0:
        return None

    head = ListNode(arr[0])
    ptr = head
    for i in range(1, n):
        ptr.next = ListNode(arr[i])
        ptr = ptr.next

    return head


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        >>> fn = Solution().addTwoNumbers
        >>> printLList(fn(createLList([2,4,3]), createLList([5,6,4])))
        7->0->8
        >>> printLList(fn(createLList([2,4,3]), createLList([5,6])))
        7->0->4
        >>> printLList(fn(createLList([0]), createLList([5,6,4])))
        5->6->4
        >>> printLList(fn(createLList([1]), createLList([9,9])))
        0->0->1
        """
        cur_l, cur_r = l1, l2
        cur = ret = ListNode(0)
        add = 0

        while cur_l or cur_r or add:
            if cur_l:
                add += cur_l.val
                cur_l = cur_l.next

            if cur_r:
                add += cur_r.val
                cur_r = cur_r.next

            val = add % 10
            add = add // 10

            cur.next = ListNode(val)
            cur = cur.next

        return ret.next


if __name__ == "__main__":
    import doctest
    doctest.testmod()
