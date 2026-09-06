# 106. Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Accepted: 2026-09-06T15:01:58.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 3 ms · Beats 73.09%
# Memory: 20.8 MB · Beats 95.42%
# Submission: https://leetcode.com/submissions/detail/2132973246/

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
        self.post_order = n-1

        def aux (left, right) : 
            if left <= right : 
                root_val = postorder[self.post_order]
                root_index = inorder[root_val]
                self.post_order-=1
                right_tree = aux(root_index +1, right)
                left_tree = aux(left, root_index -1 )
                return TreeNode(root_val, left_tree, right_tree)
            else :
                return None
        
        return aux(0, n-1)
