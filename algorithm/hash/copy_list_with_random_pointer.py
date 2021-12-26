"""
https://leetcode.com/problems/copy-list-with-random-pointer/
138. Copy List with Random Pointer
Medium

A linked list is given such that each node contains an additional 
random pointer which could point to any node in the list or null.

Return a deep copy of the list.


https://discuss.leetcode.com/uploads/files/1470150906153-2yxeznm.png

Example 1:

Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer
points to itself.
 

Note:
You must return the copy of the given head as a reference to the cloned list.
"""


from collections import defaultdict


class Solution:
    def copyRandomList2(self, head: 'Node') -> 'Node':
        """O(N), O(N)
        """
        d = defaultdict(lambda: Node(0, None, None))
        cur, d[None] = head, None
        while cur:
            d[cur].val = cur.val
            d[cur].next = d[cur.next]
            d[cur].random = d[cur.random]
            cur = cur.next
        return d[head]           
        
    def copyRandomList1(self, head: 'Node') -> 'Node':
        """O(N), O(N)
        """
        cur1 = dummy = Node(0, None, None)
        cur2, dic = head, {None: None}
        while cur2:
            dic[cur2] = cur1.next = Node(cur2.val, cur2.next, cur2.random)
            cur1, cur2 = cur1.next, cur2.next  
        cur1 = dummy.next
        while cur1:
            cur1.random = dic[cur1.random]
            cur1 = cur1.next
        return dummy.next
        
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
