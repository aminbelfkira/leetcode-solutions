# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/
# Accepted: 2026-09-21T12:44:13.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 20 MB · Beats 44.89%
# Submission: https://leetcode.com/submissions/detail/2148633592/

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n
        while left < right :
            mid = (left + right)//2

            if nums[mid] < target : 
                left = mid +1
            else : 
                right = mid
        return left 
