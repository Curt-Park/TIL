"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

236. Lowest Common Ancestor of a Binary Tree
Medium

Given a binary tree, find the lowest common ancestor (LCA) of
two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest 
common ancestor is defined between two nodes p and q as the 
lowest node in T that has both p and q as descendants 
(where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

       3
   5       1
 6.  2.  0.  8
n n 7 4 n n n n

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node 
can be a descendant of itself according to the LCA definition.
 

Note:
All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.

3 5 6 2 7 4 1 0 8
3 1 8 0 5 2 4 7 6
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """O(N), O(H)"""
        def traverse(node: 'TreeNode', p_val: int, q_val: int, ret: 'TreeNode') -> bool:
            if not node:
                return False
            cnt = (
                (node.val == p_val) + 
                (node.val == q_val) + 
                traverse(node.left, p_val, q_val, ret) + 
                traverse(node.right, p_val, q_val, ret)
            )
            if cnt == 2:
                ret.val = node.val
            return True if cnt > 0 else False
        ret = TreeNode(0)
        traverse(root, p.val, q.val, ret)
        return ret
