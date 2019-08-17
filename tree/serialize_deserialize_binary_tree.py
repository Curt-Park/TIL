"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

297. Serialize and Deserialize Binary Tree
Hard

Serialization is the process of converting a data structure or 
object into a sequence of bits so that it can be stored in a file 
or memory buffer, or transmitted across a network connection link 
to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your serialization/deserialization 
algorithm should work. You just need to ensure that a binary tree 
can be serialized to a string and this string can be deserialized 
to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode 
serializes a binary tree. You do not necessarily need to follow this format, 
so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. 
Your serialize and deserialize algorithms should be stateless.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Codec2:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def traverse(node, s):
            s.append(str(node.val) if node else "n")
            if not node:
                return
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
        def traverse(s):
            if not s:
                return None
            v = s.pop()
            if v == "n":
                return None
            node = TreeNode(int(v))
            node.left, node.right = traverse(s), traverse(s)
            return node
        return traverse(data.split()[::-1])


class Codec1:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        stack, ret = [root], [str(id(root))]
        while stack:
            node = stack.pop()
            if not node:
                continue
            val, left, right = node.val, node.left, node.right
            s = ",".join(map(str, [id(node), val, id(left), id(right)]))
            ret.append(s)
            stack.extend([left, right])
        return "/".join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        d, stream = defaultdict(lambda : TreeNode(0)), data.split("/")
        root, d[id(None)] = int(stream[0]), None
        for s in stream[1:]:
            node, val, left, right = map(int, s.split(","))
            d[node].val = val
            d[node].left = d[left]
            d[node].right = d[right]
        return d[root]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
