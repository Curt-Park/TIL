"""
https://leetcode.com/problems/diameter-of-binary-tree/

543. Diameter of Binary Tree
Easy

Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """O(N) / O(H)"""
        def traverse(node: TreeNode) -> int:
            if not node: return 0
            ll, rl = traverse(node.left), traverse(node.right)
            self.longest_path = max(self.longest_path, ll + rl)
            return 1 + max(ll, rl)
        self.longest_path = 0; traverse(root)
        return self.longest_path
