# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# Accepted: 2026-10-06T12:18:06.000Z
# Language: Python3
# Runtime: 39 ms · Beats 48.2%
# Memory: 31.5 MB · Beats 21.83%
# Submission: https://leetcode.com/submissions/detail/2164204673/

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        
        max_sum = - float('inf')
        current_sum = - float('inf')
        for num in nums : 
            current_sum = max(current_sum + num, num)
            max_sum = max(max_sum, current_sum)
        return max_sum
