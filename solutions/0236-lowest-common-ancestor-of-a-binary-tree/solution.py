# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Accepted: 2026-09-14T12:58:12.000Z
# Language: Python3
# Runtime: 124 ms · Beats 85.7%
# Memory: 50.7 MB · Beats 69.2%
# Submission: https://leetcode.com/submissions/detail/2141567751/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root is None or root is p or root is q : 
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None : 
            return root
        
        return left or right
