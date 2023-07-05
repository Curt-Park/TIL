package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func sortList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	slow, fast := head, head.Next
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	left, right := head, slow.Next
	slow.Next = nil

	dummy := &ListNode{}
	ptr, lPtr, rPtr := dummy, sortList(left), sortList(right)
	for lPtr != nil && rPtr != nil {
		if lPtr.Val > rPtr.Val {
			ptr.Next = rPtr
			rPtr = rPtr.Next
		} else {
			ptr.Next = lPtr
			lPtr = lPtr.Next
		}
		ptr = ptr.Next
	}
	if lPtr != nil {
		ptr.Next = lPtr
	} else {
		ptr.Next = rPtr
	}
	return dummy.Next
}
