package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getIntersectionNode(headA, headB *ListNode) *ListNode {
	ptrA, ptrB := headA, headB
	for ptrA != nil && ptrB != nil {
		ptrA = ptrA.Next
		ptrB = ptrB.Next
	}
	short, long := headA, headB
	if ptrA != nil {
		ptrA, ptrB = ptrB, ptrA
		long, short = short, long
	}
	for ptrB != nil {
		long = long.Next
		ptrB = ptrB.Next
	}
	for short != nil && long != nil {
		if short == long {
			return short
		}
		short = short.Next
		long = long.Next
	}
	return nil
}
