# 108. Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Accepted: 2026-09-13T17:47:23.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 3 ms · Beats 48.81%
# Memory: 20.4 MB · Beats 6.33%
# Submission: https://leetcode.com/submissions/detail/2140875387/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def build(left, right) :
            if left > right : 
                return None
            
            mid = (left + right) //2
            return TreeNode(nums[mid], build(left, mid -1), build(mid+1, right))
        
        return build(0, len(nums)-1)
