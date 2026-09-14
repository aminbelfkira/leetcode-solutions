# 108. Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Accepted: 2026-09-14T21:23:42.000Z
# Language: Python3
# Runtime: 3 ms · Beats 48.83%
# Memory: 20.4 MB · Beats 6.38%
# Submission: https://leetcode.com/submissions/detail/2142011151/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums :
            return None

        left = 0
        right = len(nums) -1
        mid = (left + right) // 2

        return TreeNode(nums[mid], self.sortedArrayToBST(nums[left : mid]), self.sortedArrayToBST(nums[mid+1: right+1]))


        
