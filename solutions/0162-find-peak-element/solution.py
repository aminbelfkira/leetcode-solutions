# 162. Find Peak Element
# https://leetcode.com/problems/find-peak-element/
# Accepted: 2026-09-21T12:52:52.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 80.66%
# Submission: https://leetcode.com/submissions/detail/2148640437/

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1

        while left < right : 
            mid = (left + right)//2
            if nums[mid] < nums[mid+1] : 
                left = mid +1
            else :
                right = mid
        return left
