# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Accepted: 2026-09-18T12:25:54.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 20.6 MB · Beats 61.98%
# Submission: https://leetcode.com/submissions/detail/2145721261/

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        ##first position : 

        left = 0 
        right = n-1

        while left < right : 
            mid = (left+right) //2
            if nums[mid] < target: 
                left = mid +1
            else : 
                right = mid
        
        first = left
        if first == len(nums) or nums[first] != target : 
            return [-1,-1]

        left, right = first, len(nums)
        while left < right : 
            mid = (left + right)//2
            if nums[mid] <= target : 
                left = mid +1
            else : 
                right = mid
        return [first, left -1]



        
