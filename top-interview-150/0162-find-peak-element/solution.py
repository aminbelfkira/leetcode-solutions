# 162. Find Peak Element
# https://leetcode.com/problems/find-peak-element/
# Accepted: 2026-09-13T19:07:15.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 41.13%
# Submission: https://leetcode.com/submissions/detail/2140950520/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) -1

        while left < right :
            mid = (left + right) //2
            if nums[mid] < nums[mid +1] :
                left = mid +1
            else :
                right = mid
        return left
