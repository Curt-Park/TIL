"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

103. Binary Tree Zigzag Level Order Traversal
Medium

Given a binary tree, return the zigzag level order traversal of 
its nodes' values. (ie, from left to right, then right to left 
for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
   
return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]

3 20 9 15 7
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """O(N), O(N)"""
        bfs, ret, order = deque([root]), [], -1
        while bfs and bfs[0]:
            zz, n, order = [], len(bfs), order * -1
            for node in [bfs.popleft() for _ in range(n)]:
                zz.append(node.val)
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
            if zz:
                ret.append(zz[::order])
        return ret
