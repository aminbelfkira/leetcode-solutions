# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Accepted: 2026-09-14T20:23:30.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 20.1 MB · Beats 25.2%
# Submission: https://leetcode.com/submissions/detail/2141984351/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        level = [root] if root else []

        while level : 
            level_val = [n.val for n in level]
            res.append(level_val)
            level = [c for child in level for c in (child.left, child.right) if c is not None]
        return res
