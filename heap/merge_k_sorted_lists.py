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

import heapq
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
    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        """ O(NlogK), O(logK)
        >>> fn = Solution().mergeKLists2
        >>> printLList(fn([createLList([1,4,5]), createLList([1,3,4]), createLList([2,6])]))
        1->1->2->3->4->4->5->6
        >>> printLList(fn([]))
        None
        >>> printLList(fn([None]))
        None
        >>> printLList(fn([None, None]))
        None
        """
        def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
            cur = dummy = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    cur, l1 = cur.next, l1.next
                else:
                    cur.next = l2
                    cur, l2 = cur.next, l2.next
            cur.next = l1 if l1 else l2
            return dummy.next

        n = len(lists)
        if n <= 1:
            return lists[0] if n == 1 else None
        l1 = self.mergeKLists2(lists[:n//2])
        l2 = self.mergeKLists2(lists[n//2:])
        return merge_two_lists(l1, l2)


    def mergeKLists1(self, lists: List[ListNode]) -> ListNode:
        """ O(NlogK), O(K)
        >>> fn = Solution().mergeKLists1
        >>> printLList(fn([createLList([1,4,5]), createLList([1,3,4]), createLList([2,6])]))
        1->1->2->3->4->4->5->6
        >>> printLList(fn([None]))
        None
        >>> printLList(fn([None, None]))
        None
        """
        class HeapElem:
            def __init__(self, node: ListNode):
                self.node = node

            def __lt__(self, other: 'HeapElem'):
                return self.node.val < other.node.val

        cur = dummy = ListNode(0)
        heap = [HeapElem(head) for head in lists if head]
        heapq.heapify(heap)
        while heap:
            node = heapq.heappop(heap).node
            cur.next = node
            cur = cur.next
            if node.next:
                node = node.next
                heapq.heappush(heap, HeapElem(node))
        return dummy.next


if __name__ == "__main__":
    import doctest
    doctest.testmod()
