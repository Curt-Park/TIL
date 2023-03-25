/*
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func swapPairs(head *ListNode) *ListNode {
	dummy := &ListNode{0, head}
	cur, next := dummy, head
	for next != nil && next.Next != nil {
		cur.Next = next.Next
		next.Next = cur.Next.Next
		cur.Next.Next = next
		cur = next
		next = next.Next
	}
	return dummy.Next
}
