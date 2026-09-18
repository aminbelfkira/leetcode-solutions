# 530. Minimum Absolute Difference in BST
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/
# Accepted: 2026-09-18T13:52:08.000Z
# Language: Python3
# Runtime: 3 ms · Beats 64.26%
# Memory: 21 MB · Beats 8.81%
# Submission: https://leetcode.com/submissions/detail/2145788705/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float('inf')

        prev = None 
        current = root
        stack = []
        while current is not None or stack: 
            while current is not None :
                stack.append(current)
                current = current.left
            current = stack.pop()
            if prev is not None : 
                min_diff = min(min_diff, current.val - prev.val)
            prev = current
            current = current.right
        return min_diff 
