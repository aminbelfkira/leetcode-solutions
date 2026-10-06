# 105. Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Accepted: 2026-10-06T12:42:31.000Z
# Language: Python3
# Runtime: 2 ms · Beats 81.67%
# Memory: 20.8 MB · Beats 93.12%
# Submission: https://leetcode.com/submissions/detail/2164223670/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        inorder_idx = {val :i for i,val in enumerate(inorder)}
        self.preorder_idx = 0

        def aux(left, right) : 
            if left > right :
                return None
            root_val = preorder[self.preorder_idx]
            self.preorder_idx +=1
            root_idx = inorder_idx[root_val]
            left_tree = aux(left, root_idx -1)
            right_tree = aux(root_idx +1, right)
            return TreeNode(root_val, left_tree, right_tree)
        
        return aux(0, len(inorder) -1)
