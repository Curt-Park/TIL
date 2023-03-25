/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	var f func(*ListNode) int
	f = func(p *ListNode) int {
		if p == nil {
			return 0
		}
		i := f(p.Next) + 1
		if i == n+1 {
			p.Next = p.Next.Next
		}
		return i
	}
	dummy := &ListNode{0, head}
	f(dummy)
	return dummy.Next
}
