# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/
# Accepted: 2026-09-18T13:10:44.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 22.9%
# Submission: https://leetcode.com/submissions/detail/2145754043/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root : 
            return root
        
        return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left))
