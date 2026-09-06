# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/
# Accepted: 2026-09-06T12:06:15.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 61.9%
# Submission: https://leetcode.com/submissions/detail/2132811953/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root :
            return root

        return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left))
