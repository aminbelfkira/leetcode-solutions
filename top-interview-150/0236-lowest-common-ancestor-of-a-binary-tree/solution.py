# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Accepted: 2026-09-12T13:46:47.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 120 ms · Beats 92.86%
# Memory: 50.7 MB · Beats 69.21%
# Submission: https://leetcode.com/submissions/detail/2139536076/

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

        left = self.lowestCommonAncestor(root.left, p,q)
        right = self.lowestCommonAncestor(root.right, p,q)

        if left is not None and right is not None : 
            return root
        
        return left or right
