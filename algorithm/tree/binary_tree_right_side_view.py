"""
https://leetcode.com/problems/binary-tree-right-side-view/

199. Binary Tree Right Side View
Medium

Given a binary tree, imagine yourself standing on 
the right side of it, return the values of the nodes 
you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import deque


class Solution(object):
    def rightSideView2(self, root):
        """ O(N), O(N)
        :type root: TreeNode
        :rtype: List[int]
        """
        dfs, ret = [(root, 1)], []
        while dfs and dfs[-1][0]:
            node, lev = dfs.pop()
            if len(ret) < lev:
                ret.append(node.val)
            else:
                ret[lev - 1] = node.val
            if node.right:
                dfs.append((node.right, lev + 1))
            if node.left:
                dfs.append((node.left, lev + 1))
        return ret
        
    def rightSideView1(self, root):
        """ O(N), O(N)
        :type root: TreeNode
        :rtype: List[int]
        """
        bst, ret = deque([root]), []
        while bst and bst[0]:
            n = len(bst)
            ret.append(bst[0].val)
            for node in [bst.popleft() for _ in range(n)]:
                if node.right:
                    bst.append(node.right)
                if node.left:
                    bst.append(node.left)
        return ret
