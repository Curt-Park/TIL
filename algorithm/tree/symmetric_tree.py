"""
https://leetcode.com/problems/symmetric-tree/

101. Symmetric Tree
Easy

Given a binary tree, check whether it is a mirror of itself 
(ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Note:
Bonus points if you could solve it both recursively and iteratively.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric2(self, root: TreeNode) -> bool:
        """O(N), O(H)"""
        def traverse(l_node, r_node) -> bool:
            if l_node and r_node and l_node.val == r_node.val:
                return (
                    traverse(l_node.left, r_node.right) and
                    traverse(r_node.left, l_node.right)
                )
            return l_node == r_node == None
        return not root or traverse(root.left, root.right)
        
    def isSymmetric1(self, root: TreeNode) -> bool:
        """O(N), O(N)"""
        def traverse(node, next, trav):
            trav.append(node.val if node else None)
            for child in next(node): traverse(child, next, trav)
        trav_l, trav_r = [], []
        traverse(root, lambda n: [n.left, n.right] if n else [], trav_l)
        traverse(root, lambda n: [n.right, n.left] if n else [], trav_r)
        return trav_l == trav_r
