# 103. Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Accepted: 2026-09-21T13:10:11.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 84.82%
# Submission: https://leetcode.com/submissions/detail/2148655198/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        
        level = [root] if root else []
        direction = 1
        res = []
        while level : 
            level_values = [n.val for n in level[::direction]]
            res.append(level_values)
            level = [c for child in level for c in (child.left, child.right) if c is not None]
            direction = -direction 
        return res
