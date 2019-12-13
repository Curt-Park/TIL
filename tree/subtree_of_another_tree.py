"""
https://leetcode.com/problems/subtree-of-another-tree/

572. Subtree of Another Tree
Easy

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        """O(|S|+|T|) / O(|S|+|T|)"""
        def convert(node: TreeNode, ret: List[str]):
            if not node:
                ret.append("|N")
                return
            ret.append(f"|{node.val}"); convert(node.left, ret); convert(node.right, ret)
        s_str, t_str = [], []; convert(s, s_str); convert(t, t_str)
        return "".join(t_str) in "".join(s_str)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        """O(|S|*|T|) / O(log|S|)"""
        def isIdentical(s: TreeNode, t: TreeNode) -> bool:
            if not s and not t: return True
            if not s and t or s and not t: return False
            return s.val == t.val and isIdentical(s.left, t.left) and isIdentical(s.right, t.right)
        return s and (isIdentical(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t))
