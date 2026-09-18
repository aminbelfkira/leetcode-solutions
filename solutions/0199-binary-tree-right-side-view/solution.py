# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/
# Accepted: 2026-09-18T13:39:01.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 33.9%
# Submission: https://leetcode.com/submissions/detail/2145777381/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        level = [root] if root else []
        res = []

        while level : 
            res.append(level[-1].val)
            level = [c for child in level for c in (child.left, child.right) if c is not None]
        return res
