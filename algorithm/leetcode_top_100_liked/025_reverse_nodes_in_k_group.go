/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseKGroup(head *ListNode, k int) *ListNode {
	if head == nil {
		return nil
	}
	cnt, p := 0, head
	for p != nil && cnt != k {
		p, cnt = p.Next, cnt+1
	}
	if cnt != k {
		return head
	}
	prev, newHead := reverse(head, k)
	head.Next = reverseKGroup(newHead, k)
	return prev
}

func reverse(cur *ListNode, k int) (*ListNode, *ListNode) {
	prev := (*ListNode)(nil)
	for i := k; i > 0; i-- {
		next := cur.Next
		cur.Next = prev
		prev = cur
		cur = next
	}
	return prev, cur
}
