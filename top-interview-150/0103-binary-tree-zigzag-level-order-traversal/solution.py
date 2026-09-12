# 103. Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Accepted: 2026-09-12T17:57:31.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.5 MB · Beats 15.88%
# Submission: https://leetcode.com/submissions/detail/2139873928/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        direction = 1
        res = []
        level = [root] if root is not None else []
        while level : 
            level_values = [n.val for n in level]
            res.append(level_values[::direction])
            direction = -direction
            level = [child for node in level for child in (node.left, node.right) if child is not None]
        
        return res
