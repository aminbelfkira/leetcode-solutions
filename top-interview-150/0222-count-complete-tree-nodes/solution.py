# 222. Count Complete Tree Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/
# Accepted: 2026-09-12T13:30:59.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 1 ms · Beats 24.92%
# Memory: 23.8 MB · Beats 21.99%
# Submission: https://leetcode.com/submissions/detail/2139522937/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        def get_left_height(node) : 
            height = 0
            while node : 
                height +=1
                node = node.left
            return height
    
        def get_right_height(node) : 
            height = 0 
            while node : 
                height +=1
                node = node.right
            return height
        
        left_height = get_left_height(root)
        right_height = get_right_height(root)

        if left_height == right_height : 
            return 2**left_height -1
        
        return (1 + self.countNodes(root.left) + self.countNodes(root.right))

