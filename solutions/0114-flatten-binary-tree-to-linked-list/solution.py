# 114. Flatten Binary Tree to Linked List
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Accepted: 2026-09-18T12:54:07.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.8 MB · Beats 5.24%
# Submission: https://leetcode.com/submissions/detail/2145741381/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        def preorder(node) :
            if not node : 
                return
            nodes.append(node)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        for i in range(len(nodes)-1) : 
            nodes[i].left = None
            nodes[i].right = nodes[i+1]
        
        if nodes : 
            nodes[-1].left = None
            nodes[-1].right = None

