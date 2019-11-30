"""
https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

1130. Minimum Cost Tree From Leaf Values
Medium

Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.  (Recall that a node is a leaf if and only if it has 0 children.)
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.  It is guaranteed this sum fits into a 32-bit integer.



Example 1:

Input: arr = [6,2,4]
Output: 32
Explanation:
There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4


Constraints:

2 <= arr.length <= 40
1 <= arr[i] <= 15
It is guaranteed that the answer fits into a 32-bit signed integer (ie. it is less than 2^31).
"""


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        """O(N^3) / O(N^2)"""
        def mct(s = 0, e = len(arr) - 1, n = float("inf"), dp0 = {}, dp1 = {}):
            if (s, e) in dp0 or e <= s:
                return s < e and dp0[s, e]
            for k in range(s + 1, e + 1):
                max_l = dp1[s, k] if (s, k) in dp1 else max(arr[s:k])
                max_r = dp1[k, e+1] if (k, e+1) in dp1 else max(arr[k:e+1])
                n = min(n, mct(s, k - 1) + mct(k, e) + max_l * max_r)
            return dp0.setdefault((s, e), n)
        return mct()
