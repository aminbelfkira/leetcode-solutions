# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/
# Accepted: 2026-09-18T14:15:00.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 20.7 MB · Beats 95.4%
# Submission: https://leetcode.com/submissions/detail/2145808036/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        prev = None
        current = root 
        stack = []

        while current is not None or stack :
            while current is not None : 
                stack.append(current)
                current = current.left
            current = stack.pop()
            if prev is not None and prev.val >= current.val : 
                return False
            prev = current
            current = current.right
        
        return True
