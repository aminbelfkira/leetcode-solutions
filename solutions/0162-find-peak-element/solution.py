# 162. Find Peak Element
# https://leetcode.com/problems/find-peak-element/
# Accepted: 2026-09-15T15:23:21.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.5 MB · Beats 11.31%
# Submission: https://leetcode.com/submissions/detail/2142741130/

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right : 
            mid = (left+right) //2
            if nums[mid] < nums[mid+1] : 
                left = mid +1
            else :
                right = mid
        return left
