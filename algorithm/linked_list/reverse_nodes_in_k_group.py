"""
https://leetcode.com/problems/reverse-nodes-in-k-group/

25. Reverse Nodes in k-Group
Hard

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:
Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """O(N) / O(1)"""
        cnt, prev, cur = 0, head, head
        while prev and cnt < k:
            prev, cnt = prev.next, cnt + 1
        if cnt < k:
            return head
        while cur and cnt:
            cur.next, prev, cur, cnt = prev, cur, cur.next, cnt - 1
        head.next = self.reverseKGroup(cur, k)
        return prev
