# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/
# Accepted: 2026-10-06T12:21:03.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.8 MB · Beats 82.44%
# Submission: https://leetcode.com/submissions/detail/2164206871/

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right : 
            mid = (left +right) //2 
            if nums[mid]< target : 
                left = mid +1
            else : 
                right = mid 
        
        return left
