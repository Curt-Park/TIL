"""
https://leetcode.com/problems/count-complete-tree-nodes/

222. Count Complete Tree Nodes
Medium

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled,
and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""


class Solution:
    def countNodes2(self, root: TreeNode) -> int:
        """O(log^2N) / O(logN)"""
        if not root:
            return 0
        l_h, r_h, l_node, r_node = 0, 0, root, root
        while l_node:
            l_h, l_node = l_h + 1, l_node.left
        while r_node:
            r_h, r_node = r_h + 1, r_node.right
        if l_h == r_h:
            return 2 ** l_h - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

    def countNodes1(self, root: TreeNode) -> int:
        """O(N) / O(logN)"""
        return 1 + self.countNodes(root.left) + self.countNodes(root.right) if root else 0
