"""
https://leetcode.com/problems/path-sum-iii/

437. Path Sum III
Medium

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        """O(N) / O(N)"""
        def dfs(node, path = [], total = 0, mem = {0: 1}):
            if not node: return 0
            path.append(node.val)
            total += node.val
            cnt = mem.get(total - target, 0)
            mem[total] = mem.get(total, 0) + 1
            cnt += dfs(node.left, path, total)
            cnt += dfs(node.right, path, total)
            mem[total] -= 1
            path.pop()
            return cnt
        return dfs(root)
