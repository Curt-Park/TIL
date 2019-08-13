"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/

124. Binary Tree Maximum Path Sum
Hard

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes 
from some starting node to any node in the tree along 
the parent-child connections. The path must contain 
at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def recPathSum(node: TreeNode) -> int:
            if not node:
                return 0
            tot_l = max(node.val, node.val + recPathSum(node.left))
            tot_r = max(node.val, node.val + recPathSum(node.right))
            self.max_sum = max(self.max_sum, tot_l + tot_r - node.val)
            return max(tot_l, tot_r)
        self.max_sum = root.val
        recPathSum(root)
        return self.max_sum
