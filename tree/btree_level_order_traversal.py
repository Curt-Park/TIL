"""
https://leetcode.com/problems/binary-tree-level-order-traversal/

102. Binary Tree Level Order Traversal
Medium

Given a binary tree, return the level order traversal of
its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderDFS(self, root: TreeNode) -> List[List[int]]:
        """O(N) / O(N)"""
        stack, ret = [(root, 0)], []
        while stack and stack[0][0]:
            n, lev = stack.pop()
            if len(ret) - 1 < lev:
                ret.append([])
            ret[lev].append(n.val)
            stack += [(c, lev+1) for c in [n.right, n.left] if c]
        return ret

    def levelOrderBFS(self, root: TreeNode) -> List[List[int]]:
        """O(N) / O(N)"""
        q, ret = [root], []
        while q and q[0]:
            ret.append([n.val for n in q])
            q = [c for n in q for c in [n.left, n.right] if c]
        return ret
