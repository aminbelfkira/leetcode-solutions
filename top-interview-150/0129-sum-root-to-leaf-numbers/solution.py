# 129. Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/
# Accepted: 2026-09-12T13:15:13.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 7.57%
# Submission: https://leetcode.com/submissions/detail/2139510211/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []

        def aux(node, current) : 
            if not node : 
                return
            if not node.left and not node.right : 
                res.append(current * 10 + node.val)
            aux(node.left, current*10 + node.val)
            aux(node.right, current*10 + node.val)
        aux(root, 0)
        return sum(res)

        
