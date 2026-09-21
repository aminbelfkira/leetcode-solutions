# 112. Path Sum
# https://leetcode.com/problems/path-sum/
# Accepted: 2026-09-21T11:33:28.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 20.1 MB · Beats 89.68%
# Submission: https://leetcode.com/submissions/detail/2148582948/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        
        def aux(node, remaining) : 
            if node is None :
                return False
            new_remaining = remaining - node.val
            if node.left is None and node.right is None : 
                return new_remaining == 0 
            return aux(node.left, new_remaining) or aux(node.right, new_remaining)
        
        return aux(root, targetSum)
