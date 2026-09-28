# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Accepted: 2026-09-28T15:10:42.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.5 MB · Beats 40.53%
# Submission: https://leetcode.com/submissions/detail/2156111170/

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        left = 0 
        right = n-1

        while left <= right : 

            mid = (left + right)//2
            if nums[mid] == target : 
                return mid

            if nums[mid] >= nums[left] : 
                if nums[left] <= target <= nums[mid] : 
                    right = mid -1
                else :
                    left = mid +1
            else : 
                if nums[mid] <target <= nums[right] : 
                    left = mid +1
                else : 
                    right = mid-1 
        return -1  
        
