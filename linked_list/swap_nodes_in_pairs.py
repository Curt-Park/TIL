"""
https://leetcode.com/problems/swap-nodes-in-pairs/

24. Swap Nodes in Pairs
Medium

Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """O(N) / O(1)"""
        dummy = ptr = ListNode(0)
        dummy.next = head
        while ptr.next and ptr.next.next:
            tmp = ptr.next
            ptr.next = ptr.next.next
            tmp.next = ptr.next.next
            ptr.next.next = tmp
            ptr = ptr.next.next
        return dummy.next
