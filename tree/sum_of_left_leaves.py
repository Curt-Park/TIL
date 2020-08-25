"""
Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        """O(N) / O(N)"""
        def dfs(node: TreeNode, is_left: bool = False) -> int:
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return is_left * node.val
            return dfs(node.left, True) + dfs(node.right, False)
        return dfs(root)
