"""
https://leetcode.com/problems/validate-binary-search-tree/

98. Validate Binary Search Tree
Medium

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """O(N), O(N)"""
        self.min_d, self.max_d = {}, {}
        def traverse(node: TreeNode) -> bool:
            if not node:
                return True
            if not (traverse(node.left) and traverse(node.right)):
                return False
            max_v = min_v = node.val
            if node.left:
                if not self.max_d[node.left] < node.val:
                    return False
                min_v = self.min_d[node.left]
            if node.right: 
                if not node.val < self.min_d[node.right]:
                    return False
                max_v = self.max_d[node.right]
            self.min_d[node], self.max_d[node] = min_v, max_v
            return True 
        return traverse(root)
