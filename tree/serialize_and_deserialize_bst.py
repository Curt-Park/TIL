"""
https://leetcode.com/problems/serialize-and-deserialize-bst/

449. Serialize and Deserialize BST
Medium

Serialization is the process of converting a data structure or 
object into a sequence of bits so that it can be stored in a file or 
memory buffer, or transmitted across a network connection link to be 
reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. 
There is no restriction on how your serialization/deserialization algorithm 
should work. You just need to ensure that a binary search tree can be 
serialized to a string and this string can be deserialized to the original 
tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. 
Your serialize and deserialize algorithms should be stateless.

Example 2:

    5
   / \
  1   4
     / \
    3   6
    
s: 5 1 4 3 6
5
1
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def traverse(node, s):
            if not node:
                return
            s.append(str(node.val))
            traverse(node.left, s)
            traverse(node.right, s)
        s = []
        traverse(root, s)
        return " ".join(s)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def traverse(s, low=float("-inf"), upper=float("inf")):
            if not s or not low < float(s[-1]) < upper:
                return None
            v = int(s.pop())
            node, v = TreeNode(v), float(v)
            node.left, node.right = traverse(s, low, v), traverse(s, v, upper)
            return node
        return traverse(data.split()[::-1])
                

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
