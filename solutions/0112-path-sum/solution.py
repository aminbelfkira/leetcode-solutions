# 112. Path Sum
# https://leetcode.com/problems/path-sum/
# Accepted: 2026-09-13T21:59:56.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 20 MB · Beats 98.46%
# Submission: https://leetcode.com/submissions/detail/2141038528/

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
            if not node.left and not node.right : 
                if remaining == node.val :
                    return True
            return aux(node.left, remaining - node.val) or aux(node.right, remaining- node.val)
        
        return aux(root, targetSum)
