# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/
# Accepted: 2026-09-15T14:15:44.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.9 MB · Beats 44.23%
# Submission: https://leetcode.com/submissions/detail/2142672822/

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right : 
            mid = (left + right)//2

            if nums[mid]<target :
                left = mid +1
            else : 
                right = mid
        return left
