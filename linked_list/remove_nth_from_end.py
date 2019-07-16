"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Remove Nth Node From End of List
Medium

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
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
    def removeNthFromEndIter(self, head: ListNode, n: int) -> ListNode:
        """ O(N), O(1)
        >>> fn = Solution().removeNthFromEndIter
        >>> printLList(fn(createLList([1, 2, 3, 4, 5]), 1))
        1->2->3->4
        >>> printLList(fn(createLList([1, 2, 3, 4, 5]), 2))
        1->2->3->5
        >>> printLList(fn(createLList([1, 2]), 2))
        2
        >>> printLList(fn(createLList([1]), 1))
        None
        """
        if not head or n < 1:
            return None

        slow = ret = ListNode(0)
        fast = ret.next = head

        for i in range(n):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return ret.next



    def removeNthFromEndRec(self, head: ListNode, n: int) -> ListNode:
        """ O(N), O(N)
        >>> fn = Solution().removeNthFromEndRec
        >>> printLList(fn(createLList([1, 2, 3, 4, 5]), 1))
        1->2->3->4
        >>> printLList(fn(createLList([1, 2, 3, 4, 5]), 2))
        1->2->3->5
        >>> printLList(fn(createLList([1, 2]), 2))
        2
        >>> printLList(fn(createLList([1]), 1))
        None
        """
        if not head or n < 1:
            return None

        self.cur = ret = ListNode(0)
        ret.next = head

        def findNthFromEnd(node: ListNode, n: int) -> int:
            if not node.next:
                return 0

            cnt = 1 + findNthFromEnd(node.next, n)
            if cnt == n:
                self.cur = node

            return cnt

        findNthFromEnd(self.cur, n)
        self.cur.next = self.cur.next.next

        return ret.next

    def removeNthFromEndStack(self, head: ListNode, n: int) -> ListNode:
        """ O(N), O(N)
        >>> fn = Solution().removeNthFromEndStack
        >>> printLList(fn(createLList([1, 2, 3, 4, 5]), 1))
        1->2->3->4
        >>> printLList(fn(createLList([1, 2, 3, 4, 5]), 2))
        1->2->3->5
        >>> printLList(fn(createLList([1, 2]), 2))
        2
        >>> printLList(fn(createLList([1]), 1))
        None
        """
        if not head or n < 1:
            return None

        cur = ret = ListNode(0)
        ret.next = head
        stack = []
        while cur:
            stack.append(cur)
            cur = cur.next

        for i in range(n + 1):
            cur = stack.pop()

        cur.next = cur.next.next

        return ret.next


if __name__ == "__main__":
    import doctest
    doctest.testmod()
