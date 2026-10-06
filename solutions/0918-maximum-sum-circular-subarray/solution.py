# 918. Maximum Sum Circular Subarray
# https://leetcode.com/problems/maximum-sum-circular-subarray/
# Accepted: 2026-10-06T14:05:33.000Z
# Language: Python3
# Runtime: 46 ms · Beats 43.22%
# Memory: 24.1 MB · Beats 62.03%
# Submission: https://leetcode.com/submissions/detail/2164302879/

class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        
        max_sum = -float('inf')
        min_sum = float('inf')
        total = 0 
        current_min = 0
        current_max = 0
        for num in nums :
            current_min = min(current_min + num, num)
            min_sum = min(current_min, min_sum)
            current_max = max(current_max + num, num)
            max_sum = max(max_sum, current_max)
            total += num
        if max_sum < 0 :
            return max_sum
        return max(max_sum, total - min_sum)
