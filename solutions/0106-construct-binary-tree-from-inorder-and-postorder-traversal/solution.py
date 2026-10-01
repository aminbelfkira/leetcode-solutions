# 106. Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Accepted: 2026-10-01T13:03:26.000Z
# Language: Python3
# Runtime: 3 ms · Beats 74.82%
# Memory: 20.8 MB · Beats 93.7%
# Submission: https://leetcode.com/submissions/detail/2159209057/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        inorder_val = {val : i for (i, val) in enumerate(inorder)}
        n = len(inorder)
        self.post_order = n-1
        def aux(left, right) : 
            if left > right :
                return None
            root_val = postorder[self.post_order]
            self.post_order -=1
            root_idx = inorder_val[root_val]
            right = aux(root_idx + 1, right)
            left = aux(left, root_idx - 1)
            tree = TreeNode(root_val,left ,right )
            return tree
        return aux(0, n-1)
        
