# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Accepted: 2026-09-18T14:00:47.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 22.1 MB · Beats 87.98%
# Submission: https://leetcode.com/submissions/detail/2145796144/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        h = 0
        stack = []
        current = root

        while current is not None or stack : 
            while current is not None : 
                stack.append(current)
                current = current.left
            current = stack.pop()
            h+=1
            if k == h : 
                return current.val
            current = current.right
         
