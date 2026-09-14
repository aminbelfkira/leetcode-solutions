# 103. Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Accepted: 2026-09-14T13:18:45.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 84.45%
# Submission: https://leetcode.com/submissions/detail/2141585848/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        direction = 1
        result = []
        level = [root] if root else []

        while level :
            tmp = level[::direction]
            tmp = [t.val for t in tmp]
            result.append(tmp)
            direction = - direction
            level = [c for child in level for c in (child.left, child.right) if c is not None]
        return result
