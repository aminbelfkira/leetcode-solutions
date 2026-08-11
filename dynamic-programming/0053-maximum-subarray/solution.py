# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# Accepted: 2026-08-11T15:12:09.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 49 ms · Beats 16.44%
# Memory: 31.5 MB · Beats 19.62%
# Submission: https://leetcode.com/submissions/detail/2103014986/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        current_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum
