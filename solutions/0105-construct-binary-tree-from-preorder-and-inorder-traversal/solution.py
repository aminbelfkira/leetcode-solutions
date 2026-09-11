# 105. Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Accepted: 2026-09-11T21:20:41.000Z
# Language: Python3
# Runtime: 4 ms · Beats 60.53%
# Memory: 20.8 MB · Beats 88.52%
# Submission: https://leetcode.com/submissions/detail/2138976760/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {val : i for i , val in enumerate(inorder)}
        n = len(inorder)
        self.preorder_idx = 0

        def aux(left, right) : 
            if left > right : 
                return None
            root_val = preorder[self.preorder_idx]
            root_idx = inorder_idx[root_val]
            self.preorder_idx +=1
            left_tree = aux(left, root_idx -1)
            right_tree = aux(root_idx +1, right)
            return TreeNode(root_val, left_tree, right_tree)
        
        return aux(0, n-1)
