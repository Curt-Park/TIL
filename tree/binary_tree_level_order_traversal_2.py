"""Binary Tree Level Order Traversal II

https://leetcode.com/explore/featured/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3378/

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """O(N) / O(N)"""
        q, sol = deque([(root, 0)]), []
        while q:
            node, level = q.popleft()
            if not node: continue
            q += (node.left, level + 1), (node.right, level + 1),
            sol += [[]] * (len(sol) == level)
            sol[level] += [node.val]
        return reversed(sol)
