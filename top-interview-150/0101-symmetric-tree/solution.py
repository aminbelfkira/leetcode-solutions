# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/
# Accepted: 2026-09-06T12:09:27.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 18.83%
# Submission: https://leetcode.com/submissions/detail/2132814478/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def is_mirror(p,q) : 
            if not p and not q : 
                return True
            if p and not q : 
                return False
            if not p and q : 
                return False
            if p.val ==q.val : 
                return is_mirror(p.left, q.right) and is_mirror(p.right, q.left)
            else : 
                return False
        
        return is_mirror(root.left, root.right)
