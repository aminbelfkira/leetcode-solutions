# 162. Find Peak Element
# https://leetcode.com/problems/find-peak-element/
# Accepted: 2026-10-06T12:24:16.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.5 MB · Beats 11.72%
# Submission: https://leetcode.com/submissions/detail/2164209217/

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) -1 

        while left < right : 
            mid = (left + right)//2
            if nums[mid] < nums[mid+1] : 
                left = mid +1
            else : 
                right = mid
        return left
