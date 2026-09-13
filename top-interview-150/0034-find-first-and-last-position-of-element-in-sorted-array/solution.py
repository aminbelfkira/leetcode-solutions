# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Accepted: 2026-09-13T19:15:48.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 20.5 MB · Beats 61.46%
# Submission: https://leetcode.com/submissions/detail/2140956763/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)
        while left < right : 
            mid = (left + right) //2
            if nums[mid] < target : 
                left = mid +1
            else : 
                right = mid
        
        first = left
        if first == len(nums) or nums[first] != target : 
            return [-1, -1]
        left, right = first, len(nums) 
        while left < right : 
            mid = (left + right)//2
            if nums[mid] <= target : 
                left = mid +1
            else : 
                right = mid
        return [first, left -1]
