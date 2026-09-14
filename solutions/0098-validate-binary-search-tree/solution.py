# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/
# Accepted: 2026-09-14T13:54:52.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 21 MB · Beats 46.32%
# Submission: https://leetcode.com/submissions/detail/2141618871/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        node = root
        previous = None

        while node is not None or stack :
            while node is not None : 
                stack.append(node)
                node = node.left
            node = stack.pop()

            if previous is not None and previous >= node.val :
                return False
            previous = node.val
            node = node.right
        return True
