# 637. Average of Levels in Binary Tree
# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Accepted: 2026-09-18T14:40:02.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 20.9 MB · Beats 70.45%
# Submission: https://leetcode.com/submissions/detail/2145829312/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        
        res = []
        level = [root] if root else []

        while level : 
            level_val = [n.val for n in level]
            res.append(sum(level_val)/len(level_val))
            level = [c for child in level for c in (child.left, child.right) if c is not None]
        return res
