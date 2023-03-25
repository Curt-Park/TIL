func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	p1, p2, dummy := list1, list2, &ListNode{0, nil}
	p := dummy
	for p1 != nil || p2 != nil {
		if p2 == nil || p1 != nil && p1.Val < p2.Val {
			p.Next = &ListNode{p1.Val, nil}
			p1 = p1.Next
		} else {
			p.Next = &ListNode{p2.Val, nil}
			p2 = p2.Next
		}
		p = p.Next
	}
	return dummy.Next
}
