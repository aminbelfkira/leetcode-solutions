# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/
# Accepted: 2026-09-13T18:50:22.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 20.1 MB · Beats 11.96%
# Submission: https://leetcode.com/submissions/detail/2140937564/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0 
        right = n
        while left <right :
            mid = (left + right)//2
            if nums[mid] < target : 
                left = mid +1
            else :
                right = mid
        
        return left
