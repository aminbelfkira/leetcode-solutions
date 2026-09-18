# 222. Count Complete Tree Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/
# Accepted: 2026-09-18T13:03:06.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 23.7 MB · Beats 53.86%
# Submission: https://leetcode.com/submissions/detail/2145748182/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        
        def get_left_height(node) :
            h = 0
            while node : 
                node = node.left
                h+=1
            return h
        def get_right_height(node) : 
            h = 0
            while node : 
                node = node.right
                h+=1
            return h
        
        left = get_left_height(root)
        right = get_right_height(root)

        if left == right :
            return 2**left -1
        else :
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
