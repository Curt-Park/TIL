"""
https://leetcode.com/problems/partition-list/

Partition List

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:
    Input: head = 1->4->3->2->5->2, x = 3
    Output: 1->2->2->4->3->5
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

    while ptr != None:
        print(ptr.val, end="")
        if ptr.next != None:
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
    def partitionInplace(self, head: ListNode, x: int) -> ListNode:
        """ O(N), O(1)
        >>> fn = Solution().partitionInplace
        >>> printLList(fn(createLList([1,4,3,2,5,2]), 3))
        1->2->2->4->3->5
        >>> printLList(fn(createLList([5,4,3]), 3))
        5->4->3
        >>> printLList(fn(createLList([3,1,2]), 3))
        1->2->3
        """
        if not head:
            return None

        cur_l = head_l = ListNode(0)
        cur_r = head_r = ListNode(0)
        cur = head

        while cur:
            if cur.val < x:
                cur_l.next = cur
                cur_l = cur_l.next
            else:
                cur_r.next = cur
                cur_r = cur_r.next
            cur = cur.next

        cur_r.next = None
        cur_l.next = head_r.next

        return head_l.next
        
    def partition(self, head: ListNode, x: int) -> ListNode:
        """ O(N), O(N)
        >>> fn = Solution().partition
        >>> printLList(fn(createLList([1,4,3,2,5,2]), 3))
        1->2->2->4->3->5
        >>> printLList(fn(createLList([5,4,3]), 3))
        5->4->3
        >>> printLList(fn(createLList([3,1,2]), 3))
        1->2->3
        """
        if not head:
            return None

        cur_l = head_l = ListNode(0)
        cur_r = head_r = ListNode(0)
        cur = head

        while cur:
            if cur.val < x:
                cur_l.next = ListNode(cur.val)
                cur_l = cur_l.next
            else:
                cur_r.next = ListNode(cur.val)
                cur_r = cur_r.next
            cur = cur.next

        cur_l.next = head_r.next

        return head_l.next


if __name__ == "__main__":
    import doctest
    doctest.testmod()
