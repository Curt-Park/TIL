"""
701. Insert into a Binary Search Tree
Medium

1202

87

Add to List

Share
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.



Example 1:


Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

Example 2:

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
Example 3:

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]


Constraints:

The number of nodes in the tree will be in the range [0, 104].
-108 <= Node.val <= 108
All the values Node.val are unique.
-108 <= val <= 108
It's guaranteed that val does not exist in the original BST.
"""

class Solution:
    def insertIntoBSTRec(self, root: TreeNode, val: int) -> TreeNode:
        """O(logN) / O(logN)"""
        if root is None:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBSTRec(root.right, val)
        else:
            root.left = self.insertIntoBSTRec(root.left, val)
        return root

    def insertIntoBSTIter(self, root: TreeNode, val: int) -> TreeNode:
        """O(logN) / O(1)"""
        if root is None:
            return TreeNode(val)
        prev = cur = root
        while cur:
            prev = cur
            cur = cur.right if cur.val < val else cur.left
        if prev.val < val:
            prev.right = TreeNode(val)
        else:
            prev.left = TreeNode(val)
        return root
