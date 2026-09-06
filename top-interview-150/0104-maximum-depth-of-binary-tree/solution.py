# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Accepted: 2026-09-06T12:02:03.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 6 ms · Beats 11.12%
# Memory: 22.5 MB · Beats 45.6%
# Submission: https://leetcode.com/submissions/detail/2132808395/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root : 
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
