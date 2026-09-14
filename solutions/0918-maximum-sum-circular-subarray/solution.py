# 918. Maximum Sum Circular Subarray
# https://leetcode.com/problems/maximum-sum-circular-subarray/
# Accepted: 2026-09-14T22:08:46.000Z
# Language: Python3
# Runtime: 43 ms · Beats 62.16%
# Memory: 24.2 MB · Beats 33.21%
# Submission: https://leetcode.com/submissions/detail/2142026816/

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        current_min = 0
        current_max = 0
        max_sum = -float('inf')
        min_sum = float('inf')
        total = 0
        for num in nums : 
            current_min = min(current_min+ num, num )
            current_max = max(current_max+num, num)
            max_sum = max(max_sum, current_max)
            min_sum = min(min_sum, current_min)
            total +=num
        if max_sum < 0 :
            return max_sum 
        return max(max_sum, total -min_sum)
