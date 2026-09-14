# 530. Minimum Absolute Difference in BST
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/
# Accepted: 2026-09-14T13:28:20.000Z
# Language: Python3
# Runtime: 3 ms · Beats 64.38%
# Memory: 21 MB · Beats 31.44%
# Submission: https://leetcode.com/submissions/detail/2141594796/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float('inf')
        stack = []
        previous = None
        node = root
        while node is not None or stack : 
            while node is not None :
                stack.append(node)
                node = node.left
            node = stack.pop()
            if previous is not None : 
                min_diff = min(min_diff, node.val - previous)
            previous = node.val
            node = node.right
        return min_diff
        
