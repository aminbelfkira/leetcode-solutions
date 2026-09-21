# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# Accepted: 2026-09-21T11:39:44.000Z
# Language: Python3
# Runtime: 39 ms · Beats 47.24%
# Memory: 31.3 MB · Beats 75.09%
# Submission: https://leetcode.com/submissions/detail/2148587102/

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        
        current_sum= 0
        max_sum = -float('inf')
        for num in nums : 
            current_sum = max(current_sum + num, num)
            max_sum = max(max_sum, current_sum)
        return max_sum
