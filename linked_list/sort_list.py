"""
https://leetcode.com/problems/sort-list/

148. Sort List
Medium

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """O(NlogN) / O(1)"""
        def merge(l1: ListNode, l2: ListNode) -> ListNode:
            dummy = p = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val: p.next, l1 = l1, l1.next
                else: p.next, l2 = l2, l2.next
                p = p.next
            p.next = l1 if l1 else l2
            return dummy.next
        if not head or not head.next: return head
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
        return merge(self.sortList(head), self.sortList(slow))
