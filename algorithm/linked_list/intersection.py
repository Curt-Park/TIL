"""
https://leetcode.com/problems/intersection-of-two-linked-lists/description/

Intersection of Two Linked Lists
Easy

Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:

begin to intersect at node c1.

Example 1:

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5].
There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.


Example 2:

Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4].
There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.


Example 3:

Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5].
Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.


Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
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


def makeIntersection(headA: ListNode, headB: ListNode, n: int) -> ListNode:
    cur = headA
    while cur:
        if cur.val == n:
            break
        cur = cur.next

    curB = headB
    while curB.next:
        curB = curB.next

    curB.next = cur

    return cur


class Solution(object):
    def getIntersectionNode1(self, headA, headB) -> ListNode:
        """ O(N+M), O(1)
        :type head1, head1: ListNode
        :rtype: ListNode
        >>> fn = Solution().getIntersectionNode1
        >>> head1 = createLList([4,1,8,4,5])
        >>> head2 = createLList([5,0,1])
        >>> node = makeIntersection(head1, head2, 8)
        >>> node == fn(head1, head2)
        True
        >>> head3 = createLList([0,9,1,2,4])
        >>> head4 = createLList([3])
        >>> node = makeIntersection(head3, head4, 2)
        >>> node == fn(head3, head4)
        True
        >>> head5 = createLList([2,6,4])
        >>> head6 = createLList([1,5])
        >>> None == fn(head5, head6)
        True
        >>> head7 = createLList([2,6,4,3,5])
        >>> head8 = createLList([1,5,7])
        >>> node = makeIntersection(head7, head8, 3)
        >>> node == fn(head7, head8)
        True
        """
        if not headA or not headB:
            return None

        cur1, cur2, diff = headA, headB, 0
        while cur1:
            cur1, diff = cur1.next, diff + 1

        while cur2:
            cur2, diff = cur2.next, diff - 1

        cur1, cur2 = (headA, headB) if diff > 0 else (headB, headA)
        diff = abs(diff)

        while diff > 0:
            cur1, diff = cur1.next, diff - 1

        while cur1 != cur2:
            cur1, cur2 = cur1.next, cur2.next

        return cur1

    def getIntersectionNode2(self, headA, headB) -> ListNode:
        """ O(N+M), O(1)
        :type head1, head1: ListNode
        :rtype: ListNode
        >>> fn = Solution().getIntersectionNode2
        >>> head1 = createLList([4,1,8,4,5])
        >>> head2 = createLList([5,0,1])
        >>> node = makeIntersection(head1, head2, 8)
        >>> node == fn(head1, head2)
        True
        >>> head3 = createLList([0,9,1,2,4])
        >>> head4 = createLList([3])
        >>> node = makeIntersection(head3, head4, 2)
        >>> node == fn(head3, head4)
        True
        >>> head5 = createLList([2,6,4])
        >>> head6 = createLList([1,5])
        >>> None == fn(head5, head6)
        True
        >>> head7 = createLList([2,6,4,3,5])
        >>> head8 = createLList([1,5,7])
        >>> node = makeIntersection(head7, head8, 3)
        >>> node == fn(head7, head8)
        True
        """
        if not headA or not headB:
            return None

        cur1, cur2 = headA, headB
        while cur1 != cur2:
            cur1 = cur1.next if cur1 else headB
            cur2 = cur2.next if cur2 else headA

        return cur1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
