# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/
# Accepted: 2026-09-15T14:15:07.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 20 MB · Beats 11.9%
# Submission: https://leetcode.com/submissions/detail/2142672194/

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
        return left if left < len(nums) else right
