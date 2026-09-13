# 918. Maximum Sum Circular Subarray
# https://leetcode.com/problems/maximum-sum-circular-subarray/
# Accepted: 2026-09-13T18:40:28.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 42 ms · Beats 66.05%
# Memory: 24.1 MB · Beats 62.74%
# Submission: https://leetcode.com/submissions/detail/2140929497/

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        current_max = 0
        max_sum = -float('inf')
        current_min = 0
        min_sum = 0
        total = 0

        for num in nums :
            total += num
            current_max = max(current_max + num, num)
            max_sum = max(max_sum, current_max)
            current_min = min(current_min + num, num)
            min_sum = min(min_sum, current_min)
        
        if max_sum <0 : 
            return max_sum
        return max(max_sum, total -min_sum)


            
