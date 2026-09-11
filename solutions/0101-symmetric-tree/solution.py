# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/
# Accepted: 2026-09-11T20:59:50.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.5 MB · Beats 18.98%
# Submission: https://leetcode.com/submissions/detail/2138968732/

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
            if not p and q : 
                return False
            if p and not q : 
                return False
            if p.val != q.val : 
                return False
            return is_mirror(p.left, q.right) and is_mirror(p.right, q.left)

        return is_mirror(root.left, root.right)
