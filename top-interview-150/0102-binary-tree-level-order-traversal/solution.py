# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Accepted: 2026-09-12T15:21:45.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.9 MB · Beats 89.23%
# Submission: https://leetcode.com/submissions/detail/2139686364/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        res= []
        queue = deque([root])
        while queue : 
            len_level = len(queue) 
            level = []
            for _ in range(len_level) :
                node = queue.popleft()
                if node : 
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level : 
                res.append(level)
        return res
