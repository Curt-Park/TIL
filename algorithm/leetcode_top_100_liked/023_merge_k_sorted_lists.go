import "container/heap"

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeKLists1(lists []*ListNode) *ListNode {
	dummy := &ListNode{0, nil}
	p, nilCnt := dummy, 0
	for nilCnt < len(lists) {
		minVal, minIdx := 10*10*10*10+1, -1
		for i, node := range lists {
			if node != nil && minVal > node.Val {
				minVal = node.Val
				minIdx = i
			}
		}
		if minIdx == -1 {
			break
		}
		p.Next = &ListNode{minVal, nil}
		p = p.Next
		lists[minIdx] = lists[minIdx].Next
		if lists[minIdx] == nil {
			nilCnt += 1
		}
	}
	return dummy.Next
}

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeKLists2(lists []*ListNode) *ListNode {
	pq := make(PQ, 0)
	dummy := &ListNode{0, nil}
	p := dummy
	for _, node := range lists {
		if node != nil {
			pq = append(pq, node)
		}
	}
	heap.Init(&pq)

	for len(pq) > 0 {
		min := heap.Pop(&pq)
		minNode := min.(*ListNode)
		p.Next = &ListNode{minNode.Val, nil}
		p = p.Next

		if minNode.Next != nil {
			heap.Push(&pq, minNode.Next)
		}
	}
	return dummy.Next
}

type PQ []*ListNode

func (lists PQ) Len() int {
	return len(lists)
}

func (lists PQ) Swap(i, j int) {
	lists[i], lists[j] = lists[j], lists[i]
}

func (lists PQ) Less(i, j int) bool {
	return lists[i].Val < lists[j].Val
}

func (lists *PQ) Push(x interface{}) {
	node := x.(*ListNode)
	*lists = append(*lists, node)
}

func (lists *PQ) Pop() interface{} {
	old := *lists
	lastNode := old[len(*lists)-1]
	*lists = old[:len(*lists)-1]
	return lastNode
}
