# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Accepted: 2026-09-12T18:13:13.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 22.3 MB · Beats 23.42%
# Submission: https://leetcode.com/submissions/detail/2139891785/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root

        while node is not None or stack :
            while node is not None :
                stack.append(node)
                node = node.left
            node =stack.pop()
            k-=1
            if k ==0 : 
                return node.val
            node = node.right
