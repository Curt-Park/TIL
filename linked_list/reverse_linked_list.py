"""
https://leetcode.com/problems/reverse-linked-list/

206. Reverse Linked List
Easy

Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively.
Could you implement both?
"""


class Solution:
    def reverseList2(self, head: ListNode) -> ListNode:
        """O(N) / O(1)"""
        prev, cur = None, head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev

    def reverseList1(self, cur: ListNode, prev: ListNode = None) -> ListNode:
        """O(N) / O(1)"""
        if not cur:
            return prev
        cur.next, succ = prev, cur.next
        return self.reverseList(succ, cur)
