# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Accepted: 2026-09-14T20:10:56.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 22.4 MB · Beats 71.67%
# Submission: https://leetcode.com/submissions/detail/2141977671/

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
