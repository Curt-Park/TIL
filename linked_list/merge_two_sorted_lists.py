"""
https://leetcode.com/problems/merge-two-sorted-lists/
21. Merge Two Sorted Lists
Easy

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of
the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def createLList(arr: List) -> ListNode:
    n = len(arr)

    if n == 0:
        return None

    head = ListNode(arr[0])
    ptr = head
    for i in range(1, n):
        ptr.next = ListNode(arr[i])
        ptr = ptr.next

    return head


def printLList(head: ListNode) -> None:
    ptr = head
    if not ptr:
        print(ptr)

    while ptr:
        print(ptr.val, end="")
        if ptr.next:
            print("->", end="")
        ptr = ptr.next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        >>> fn = Solution().mergeTwoLists
        >>> printLList(fn(createLList([1,2,4]), createLList([1,3,4])))
        1->1->2->3->4->4
        """
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
