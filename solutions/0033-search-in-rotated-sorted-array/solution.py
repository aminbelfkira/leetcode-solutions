# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Accepted: 2026-09-18T12:17:57.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 77.85%
# Submission: https://leetcode.com/submissions/detail/2145715759/

class Solution:
    def search(self, nums: list[int], target: int) -> int:

        left = 0
        right = len(nums) -1

        while left <= right : 

            mid = (left + right)//2

            if nums[mid] == target :
                return mid
            if nums[mid] >= nums[left] : 
                if nums[left] <= target < nums[mid] : 
                    right = mid- 1
                else : 
                    left = mid+1
            else : 
                if nums[mid] < target <= nums[right] :
                    left = mid +1
                else : 
                    right = mid-1

        return -1 
        
