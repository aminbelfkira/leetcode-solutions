# 530. Minimum Absolute Difference in BST
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/
# Accepted: 2026-09-12T18:01:35.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 4 ms · Beats 36.98%
# Memory: 20.9 MB · Beats 31.31%
# Submission: https://leetcode.com/submissions/detail/2139878440/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        node = root
        previous = None
        min_diff = float('inf') 
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
