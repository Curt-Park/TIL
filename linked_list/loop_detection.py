"""
https://leetcode.com/problems/linked-list-cycle/description/
Linked List Cycle
Easy

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list,
we use an integer pos which represents the position (0-indexed) in the linked
list where tail connects to.
If pos is -1, then there is no cycle in the linked list.


Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list,
where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list,
where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Follow up:
Can you solve it using O(1) (i.e. constant) memory?
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


def createCycle(head: ListNode, pos: int):
    end = head
    while end.next:
        end = end.next

    cyc = head
    for _ in range(pos):
        cyc = cyc.next

    end.next = cyc


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        >>> fn = Solution().hasCycle
        """
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
