# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# Accepted: 2026-09-18T14:41:53.000Z
# Language: Python3
# Runtime: 3 ms · Beats 53.49%
# Memory: 20.9 MB · Beats 7.4%
# Submission: https://leetcode.com/submissions/detail/2145830840/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        seen = {}
        for i, num in enumerate(nums) : 
            if num in seen : 
                return [seen[num], i]
            seen[target - num] = i
