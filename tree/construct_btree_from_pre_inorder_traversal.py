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
        def traverse(i_l: int, i_r: int) -> TreeNode:
                if not i_l <= i_r: return None
                node, i = TreeNode(preorder[-1]), idx_map[preorder.pop()]
                node.left, node.right = traverse(i_l, i - 1), traverse(i + 1, i_r)
                return node
        idx_map, preorder = {v: i for i, v in enumerate(inorder)}, preorder[::-1]
        return traverse(0, len(preorder) - 1)
