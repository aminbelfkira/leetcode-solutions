# 129. Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/
# Accepted: 2026-09-18T13:44:09.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.2 MB · Beats 72.72%
# Submission: https://leetcode.com/submissions/detail/2145781820/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        res = []
        def aux(node, current) : 
            if not node :
                return
            if not node.left and not node.right : 
                res.append(current*10 + node.val)
                return
            aux(node.left, current*10 + node.val)
            aux(node.right, current*10 + node.val)
        aux(root, 0)
        print(res)
        return sum(res)
