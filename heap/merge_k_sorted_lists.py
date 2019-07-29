"""
https://leetcode.com/problems/merge-k-sorted-lists/

23. Merge k Sorted Lists
Hard

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
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
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        >>> fn = Solution().mergeKLists
        >>> printLList(fn([createLList([1,4,5]), createLList([1,3,4]), createLList([2,6])]))
        1->1->2->3->4->4->5->6
        """
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
