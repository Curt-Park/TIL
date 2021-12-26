"""
Remove Duplicates from Sorted List II
Medium
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """O(N), O(1)
        >>> s = Solution()
        >>> printLList(s.deleteDuplicates(createLList([1, 2, 3, 3, 4, 4, 5])))
        1->2->5
        >>> printLList(s.deleteDuplicates(createLList([1, 1, 1, 2, 3])))
        2->3
        >>> printLList(s.deleteDuplicates(createLList([1, 2, 2])))
        1
        >>> printLList(s.deleteDuplicates(createLList([1])))
        1
        >>> printLList(s.deleteDuplicates(createLList([1, 1, 1])))
        None
        >>> printLList(s.deleteDuplicates(createLList([])))
        None
        """
        if not head:
            return None

        pre_node = ret_node = ListNode(head.val - 1)
        pre_node.next = cur_node = head
        while cur_node:
            if cur_node.next and cur_node.val == cur_node.next.val:
                val = cur_node.val
                while cur_node and cur_node.val == val:
                    cur_node = cur_node.next
                pre_node.next = cur_node
            else:
                cur_node = cur_node.next
                pre_node = pre_node.next

        return ret_node.next

    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        """O(N), O(N)
        >>> s = Solution()
        >>> printLList(s.deleteDuplicates2(createLList([1, 2, 3, 3, 4, 4, 5])))
        1->2->5
        >>> printLList(s.deleteDuplicates2(createLList([1, 1, 1, 2, 3])))
        2->3
        >>> printLList(s.deleteDuplicates2(createLList([1, 2, 2])))
        1
        >>> printLList(s.deleteDuplicates2(createLList([1])))
        1
        >>> printLList(s.deleteDuplicates2(createLList([1, 1, 1])))
        None
        >>> printLList(s.deleteDuplicates2(createLList([])))
        None
        """
        if not head:
            return head

        counter = {}
        ptr = head
        while ptr:
            if not ptr.val in counter:
                counter[ptr.val] = 1
            else:
                counter[ptr.val] += 1

            ptr = ptr.next

        ret_node = ListNode(head.val - 1)
        ret_node.next = head
        ptr = ret_node
        while ptr:
            if ptr.next and counter[ptr.next.val] > 1:
                ptr.next = ptr.next.next
                continue

            ptr = ptr.next

        return ret_node.next


if __name__ == "__main__":
    import doctest
    doctest.testmod()
