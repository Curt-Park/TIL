"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

105. Construct Binary Tree from Preorder and Inorder Traversal
Medium

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

from collections import deque


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """O(N) / O(N)"""
        def traverse(idx_l: int, idx_r: int) -> TreeNode:
            if not idx_l <= idx_r: return None
            node = TreeNode(preorder_dq[0])
            idx = inorder_map[preorder_dq.popleft()]
            node.left = traverse(idx_l, idx - 1)
            node.right = traverse(idx + 1, idx_r)
            return node
        preorder_dq = deque(preorder)
        inorder_map = {v: i for i, v in enumerate(inorder)}
        return traverse(0, len(preorder) - 1)
