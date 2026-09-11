# 106. Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Accepted: 2026-09-11T21:15:56.000Z
# Language: Python3
# Runtime: 7 ms · Beats 44.17%
# Memory: 20.9 MB · Beats 93.68%
# Submission: https://leetcode.com/submissions/detail/2138974988/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        inorder = {val : i for i, val in enumerate(inorder)}
        n = len(inorder)
        self.postorder_idx = n-1

        def aux(left, right) : 
            if left > right :
                return None
            root_val = postorder[self.postorder_idx]
            self.postorder_idx -=1
            root_idx = inorder[root_val]
            right_tree = aux(root_idx+1, right)
            left_tree = aux(left, root_idx -1)

            return TreeNode(root_val, left_tree, right_tree)
        
        return aux(0, n-1)
