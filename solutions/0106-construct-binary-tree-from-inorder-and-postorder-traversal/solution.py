# 106. Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Accepted: 2026-09-22T06:26:22.000Z
# Language: Python3
# Runtime: 3 ms · Beats 74.65%
# Memory: 21 MB · Beats 89.12%
# Submission: https://leetcode.com/submissions/detail/2149406335/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        inorder  = {val : i for i, val in enumerate(inorder)}
        self.post_idx = len(inorder) -1

        def aux(left,right) : 
            if right < left : 
                return None
            root_val = postorder[self.post_idx]
            root_idx = inorder[root_val]
            self.post_idx -=1
            right_tree = aux(root_idx+1, right)
            left_tree = aux(left, root_idx-1)
            return TreeNode(root_val, left_tree, right_tree)
        return aux(0, len(inorder) -1)
            
        
