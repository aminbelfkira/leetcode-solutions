# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# Accepted: 2026-07-20T23:34:55.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 20.6 MB · Beats 6.98%
# Submission: https://leetcode.com/submissions/detail/2075135530/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i, num in enumerate(nums) : 

            if num in seen : 
                return [seen[num], i]
            seen[target -num] = i
         

