# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# Accepted: 2026-09-14T22:05:44.000Z
# Language: Python3
# Runtime: 30 ms · Beats 75.01%
# Memory: 31.4 MB · Beats 45.11%
# Submission: https://leetcode.com/submissions/detail/2142025880/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = -float('inf')
        best = -float('inf')
        for num in nums :
            current = max(num, current + num)
            best = max(best, current)
        return best
