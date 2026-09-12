# 637. Average of Levels in Binary Tree
# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Accepted: 2026-09-12T15:16:35.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 21 MB · Beats 37.66%
# Submission: https://leetcode.com/submissions/detail/2139676606/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        level = [root] if root else []
        while level :
            res.append(sum([n.val for n in level])/len(level))
            level = [child for node in level for child in (node.left, node.right) if child is not None]
        return res
