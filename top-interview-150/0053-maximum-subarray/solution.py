# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# Accepted: 2026-09-13T18:23:27.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 37 ms · Beats 52.07%
# Memory: 31.5 MB · Beats 44.92%
# Submission: https://leetcode.com/submissions/detail/2140913431/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = - float('inf')
        best = - float('inf')

        for num in nums : 
            current = max(num, current + num)
            best = max(best, current)
        return best
