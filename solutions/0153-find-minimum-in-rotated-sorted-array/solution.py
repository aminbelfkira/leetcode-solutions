# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Accepted: 2026-10-06T14:54:23.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.5 MB · Beats 27.57%
# Submission: https://leetcode.com/submissions/detail/2164353883/

class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0 
        right = len(nums) -1
        while left < right : 
            mid = (left + right)//2
            if nums[mid] > nums[right] :
                left = mid +1
            else : 
                right = mid
        return nums[left]
