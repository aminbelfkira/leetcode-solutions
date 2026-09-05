# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# Accepted: 2026-09-05T15:26:21.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 20.8 MB · Beats 7.2%
# Submission: https://leetcode.com/submissions/detail/2131862395/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}

        for i, num in enumerate(nums) : 
            if num in counter :
                return [i,counter[num] ]
            counter[target -num] = i
        
