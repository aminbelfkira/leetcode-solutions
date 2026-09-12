# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/
# Accepted: 2026-09-12T15:13:32.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.2 MB · Beats 93.25%
# Submission: https://leetcode.com/submissions/detail/2139670641/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        level = [root] if root is not None else []

        while level : 
            result.append(level[-1].val)
            level = [child for node in level for child in (node.left, node.right) if child is not None]
        
        return result
