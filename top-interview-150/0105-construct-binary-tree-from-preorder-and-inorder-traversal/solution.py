# 105. Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Accepted: 2026-09-06T12:16:07.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 3 ms · Beats 77.34%
# Memory: 20.8 MB · Beats 93.45%
# Submission: https://leetcode.com/submissions/detail/2132820074/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {val : i for i, val in enumerate(inorder)}

        self.pre_order = 0

        def aux(left, right) :
            if left > right : 
                return None
            root_val = preorder[self.pre_order]
            self.pre_order +=1
            mid_idx = inorder_index[root_val]
            root_left = aux(left, mid_idx -1)
            root_right = aux(mid_idx +1, right)
            return TreeNode(val = root_val, left = root_left, right = root_right)
        return aux(0, len(preorder) -1)



