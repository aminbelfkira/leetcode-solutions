# 112. Path Sum
# https://leetcode.com/problems/path-sum/
# Accepted: 2026-09-12T13:10:58.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 20.2 MB · Beats 22.05%
# Submission: https://leetcode.com/submissions/detail/2139506871/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def aux(node, remaining) :
            if not node : 
                return False
            remaining -=node.val

            if not node.left and not node.right : 
                return remaining == 0

            return aux(node.left, remaining) or aux(node.right, remaining)

        return aux(root, targetSum) 
