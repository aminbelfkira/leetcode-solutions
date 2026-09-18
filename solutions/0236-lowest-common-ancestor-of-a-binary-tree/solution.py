# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Accepted: 2026-09-18T13:35:09.000Z
# Language: Python3
# Runtime: 127 ms · Beats 78.47%
# Memory: 50.6 MB · Beats 69.22%
# Submission: https://leetcode.com/submissions/detail/2145774170/

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
        right = self.lowestCommonAncestor(root.right, p,q)

        if left is not None and right is not None :
            return root
        elif left is None : 
            return right
        else : 
            return left
