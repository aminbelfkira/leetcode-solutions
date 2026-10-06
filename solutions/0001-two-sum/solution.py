# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# Accepted: 2026-10-06T12:56:57.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 20.8 MB · Beats 7.63%
# Submission: https://leetcode.com/submissions/detail/2164235740/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        counter = {}
        for i, num in enumerate(nums) : 
            if num in counter : 
                return [counter[num], i]
            counter[target - num] = i
        
