# 530. Minimum Absolute Difference in BST
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/
# Accepted: 2026-10-01T08:52:50.000Z
# Language: Python3
# Runtime: 3 ms · Beats 64.79%
# Memory: 20.8 MB · Beats 90.61%
# Submission: https://leetcode.com/submissions/detail/2159022560/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        stack = []
        current = root 
        prev = None
        min_diff = float('inf')
        while current or stack : 

            while current is not None: 
                stack.append(current)
                current = current.left
            current = stack.pop()
            if prev is not None : 
                min_diff = min(min_diff, current.val - prev.val)
            prev = current
            current = current.right
        return min_diff

        
