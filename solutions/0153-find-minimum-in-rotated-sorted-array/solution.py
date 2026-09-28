# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Accepted: 2026-09-28T15:27:47.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 68.32%
# Submission: https://leetcode.com/submissions/detail/2156129304/

class Solution:
    def findMin(self, nums: list[int]) -> int:
        
        left =  0
        right = len(nums) -1
        while left < right :
            mid = (left + right)//2
            if nums[mid] > nums[right] : 
                left = mid +1 
            else : 
                right = mid
        return nums[left]
