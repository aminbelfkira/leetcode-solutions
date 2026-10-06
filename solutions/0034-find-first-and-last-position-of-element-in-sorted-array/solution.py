# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Accepted: 2026-10-06T14:45:43.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 20.5 MB · Beats 63.01%
# Submission: https://leetcode.com/submissions/detail/2164344871/

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        n = len(nums)
        left = 0
        right = n-1

        while left < right : 
            mid = (left + right)//2
            if nums[mid] < target : 
                left = mid +1
            else : 
                right = mid
        
        first = left 
        if left >= n or nums[first] != target: 
            return [-1,-1]
        left = 0
        right = n
        
        while left < right : 
            mid = (left + right)//2
            if nums[mid] <= target :
                left = mid +1
            else : 
                right = mid
        return [first, left -1]
        
