# 100. Same Tree
# https://leetcode.com/problems/same-tree/
# Accepted: 2026-09-06T12:03:56.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 32.5%
# Submission: https://leetcode.com/submissions/detail/2132810004/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q :
            return True
        if p and not q :
            return False
        if q and not p : 
            return False
        if q.val != p.val : 
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
