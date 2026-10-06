# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Accepted: 2026-10-06T11:53:16.000Z
# Language: Python3
# Runtime: 1 ms · Beats 27.2%
# Memory: 20 MB · Beats 62.34%
# Submission: https://leetcode.com/submissions/detail/2164186633/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        res = []
        level = [root] if root else []
        while level : 
            level_val = [c.val for c in level]
            res.append(level_val) 
            level = [c for child in level for c in (child.left, child.right) if c is not None]
        return res
