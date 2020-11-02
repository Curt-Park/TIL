"""
https://leetcode.com/problems/recover-binary-search-tree/solution/

99. Recover Binary Search Tree
Hard

Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import Callable


class Solution:
    def recoverTree2(self, root: TreeNode) -> None:
        """O(N) / O(H)
        Do not return anything, modify root in-place instead.
        """
        def traverse(node: TreeNode) -> None:
            if not node: return
            traverse(node.left)
            if self.recent and node.val < self.recent.val:
                if not self.fix: self.fix = [self.recent, node]
                else: self.fix[1] = node
            self.recent = node
            traverse(node.right)
        self.recent = self.fix = None; traverse(root)
        self.fix[0].val, self.fix[1].val = self.fix[1].val, self.fix[0].val

    def recoverTree1(self, root: TreeNode) -> None:
        """O(NH) / O(H)
        Do not return anything, modify root in-place instead.
        """
        def findNode(root: TreeNode, comp: Callable[[int, int], bool]) -> TreeNode:
            stack, node = [root], root
            while stack and stack[-1]:
                comp_node = stack.pop()
                if comp(node.val, comp_node.val): node = comp_node
                if comp_node.left: stack.append(comp_node.left)
                if comp_node.right: stack.append(comp_node.right)
            return node
        if not root: return
        l_node = findNode(root.left, lambda val0, val1: val0 < val1)
        r_node = findNode(root.right, lambda val0, val1: val0 > val1)
        condition0 = l_node and root.val < l_node.val
        condition1 = r_node and r_node.val < root.val
        if condition0 and condition1: l_node.val, r_node.val = r_node.val, l_node.val
        elif condition0: l_node.val, root.val = root.val, l_node.val
        elif condition1: r_node.val, root.val = root.val, r_node.val
        else: self.recoverTree(root.left); self.recoverTree(root.right)

    def recoverTree0(self, root: TreeNode) -> None:
        """O(N) / O(N)
        Do not return anything, modify root in-place instead.
        """
        def traverse(node: TreeNode) -> None:
            if not node:
                return
            traverse(node.left)
            log.append(node)
            traverse(node.right)
        log = []
        traverse(root)
        l, r = 0, len(log) - 1
        while log[l].val < log[l + 1].val: l += 1
        while log[r - 1].val < log[r].val: r -= 1
        log[l].val, log[r].val = log[r].val, log[l].val
