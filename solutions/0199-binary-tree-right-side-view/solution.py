# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/
# Accepted: 2026-09-14T13:07:35.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 33.71%
# Submission: https://leetcode.com/submissions/detail/2141575827/

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
            level = [c for child in level for c in (child.left, child.right) if c ]
        
        return result
