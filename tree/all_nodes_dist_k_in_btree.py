"""
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

863. All Nodes Distance K in Binary Tree
Medium

We are given a binary tree (with root node root), a target node, and an integer value K.
Return a list of the values of all nodes that have a distance K from the target node.
The answer can be returned in any order.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
Output: [7,4,1]

Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.

Note:
The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        """O(N) / O(logN)"""
        def createDistMap(node: TreeNode) -> bool:
            if not node: return False
            if node == target: return True
            if createDistMap(node.left): dist[node] = dist[node.left] + 1; return True
            if createDistMap(node.right): dist[node] = dist[node.right] + 1; return True
            return False
        def traverseK(node: TreeNode, K: int) -> None:
            if K < 0: return
            if node and not K: ans.append(node.val); return
            if node.left not in dist: traverseK(node.left, K - 1)
            if node.right not in dist: traverseK(node.right, K - 1)
        ans, dist = [], {None: K + 1, target: 0}
        createDistMap(root)
        for node in dist: traverseK(node, K - dist[node])
        return ans

    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        """O(N) / O(N)"""
        def findParent(node: TreeNode) -> None:
            if not node: return
            parent[node.left] = parent[node.right] = node
            findParent(node.left); findParent(node.right)
        def traverseK(node: TreeNode, K: int) -> None:
            if node in visited: return
            visited.add(node)
            if not K: ans.append(node.val); return
            if node in parent: traverseK(parent[node], K - 1)
            traverseK(node.left, K - 1); traverseK(node.right, K - 1)
        ans, parent, visited = [], {}, set([None])
        findParent(root); traverseK(target, K)
        return ans
