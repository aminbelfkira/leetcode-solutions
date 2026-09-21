# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/
# Accepted: 2026-09-21T13:18:28.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 55.93%
# Submission: https://leetcode.com/submissions/detail/2148662793/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def is_mirror(left, right) :
            if left is None and right is None : 
                return True
            if left is not None and right is None : 
                return False
            if left is None and right is not None : 
                return False
            if left.val != right.val : 
                return False
            return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)
        return is_mirror(root.left, root.right)
