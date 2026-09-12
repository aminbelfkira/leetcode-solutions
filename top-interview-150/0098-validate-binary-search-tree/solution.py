# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/
# Accepted: 2026-09-12T20:57:42.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 21 MB · Beats 46.35%
# Submission: https://leetcode.com/submissions/detail/2140004644/

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
        ## on utilise la proprité du bfs : son parcours infixe est trié
        while node is not None or stack :
            while node is not None :
                stack.append(node)
                node = node.left
            node = stack.pop()
            if previous is not None and node.val <= previous : 
                return False
            previous = node.val
            node = node.right
        return True
