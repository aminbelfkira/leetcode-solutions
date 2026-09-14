# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Accepted: 2026-09-14T13:39:33.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 22.1 MB · Beats 87.78%
# Submission: https://leetcode.com/submissions/detail/2141604789/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = 1 
        stack = []
        node = root

        while node is not None or stack :
            while node is not None : 
                stack.append(node) 
                node = node.left
            node = stack.pop()
            if i == k:
                return node.val
            i+=1
            node = node.right
        return -1
