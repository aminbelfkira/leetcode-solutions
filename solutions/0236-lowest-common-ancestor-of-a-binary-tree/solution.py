# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Accepted: 2026-10-07T06:51:00.000Z
# Language: Python3
# Runtime: 132 ms · Beats 62.56%
# Memory: 50.9 MB · Beats 25.61%
# Submission: https://leetcode.com/submissions/detail/2165014005/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is p or root is q or root is None : 
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None : 
            return root
        return left or right
