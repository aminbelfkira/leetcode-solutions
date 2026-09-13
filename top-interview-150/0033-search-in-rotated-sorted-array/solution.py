# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Accepted: 2026-09-13T19:11:07.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 77.64%
# Submission: https://leetcode.com/submissions/detail/2140953399/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0 , len(nums) - 1

        while left <= right :
            mid = (left + right)//2
            if nums[mid] == target :
                return mid
            
            if nums[left] <= nums[mid] : 
                if nums[left] <= target < nums[mid] : 
                    right = mid - 1
                else : 
                    left = mid +1
            else : 
                if nums[mid] < target <= nums[right] : 
                    left = mid+1
                else : 
                    right = mid -1
        return -1
