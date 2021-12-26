"""
https://leetcode.com/problems/palindrome-linked-list/description/
Palindrome Linked List
Easy

Given a singly linked list, determine if it is a palindrome.


Example 1:

Input: 1->2
Output: false


Example 2:

Input: 1->2->2->1
Output: true


Follow up:
Could you do it in O(n) time and O(1) space?
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


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """ O(N), O(1)
        >>> fn = Solution().isPalindrome
        >>> fn(createLList([]))
        True
        >>> fn(createLList([1]))
        True
        >>> fn(createLList([1, 2]))
        False
        >>> fn(createLList([2, 2]))
        True
        >>> fn(createLList([1, 2, 1]))
        True
        >>> fn(createLList([0, 2, 2, 1]))
        False
        >>> fn(createLList([1, 2, 2, 1]))
        True
        >>> fn(createLList([0, 2, 3, 2, 1]))
        False
        >>> fn(createLList([1, 2, 3, 2, 1]))
        True
        """
        # find the mid, and reverse the first half
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev, slow.next, slow, fast = slow, prev, slow.next, fast.next.next

        # split into two: half1, half2
        half1, half2 = prev, slow.next if fast else slow

        # compare: half1, half2
        while half1:
            if half1.val != half2.val:
                return False
            half1, half2 = half1.next, half2.next

        return True

    def isPalindromeArr(self, head: ListNode) -> bool:
        """ O(N), O(N)
        >>> fn = Solution().isPalindromeArr
        >>> fn(createLList([1, 2]))
        False
        >>> fn(createLList([2, 2]))
        True
        >>> fn(createLList([1, 2, 2, 1]))
        True
        >>> fn(createLList([1, 2, 3, 2, 1]))
        True
        """
        cur = head
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        return arr == arr[::-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
