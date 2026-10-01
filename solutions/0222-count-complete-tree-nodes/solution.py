# 222. Count Complete Tree Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/
# Accepted: 2026-10-01T08:41:52.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 23.9 MB · Beats 6.4%
# Submission: https://leetcode.com/submissions/detail/2159013579/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        
        def get_left_height(node) :
            if not node : 
                return 0 
            k = 0
            while node : 
                node = node.left
                k+=1
            return k  
        def get_right_height(node) :
            if not node : 
                return 0 
            k = 0
            while node : 
                node = node.right
                k+=1
            return k  
        
        left_height = get_left_height(root)
        right_height = get_right_height(root)

        if left_height == right_height : 
            return 2**left_height -1
        return 1+  self.countNodes(root.left) + self.countNodes(root.right)
