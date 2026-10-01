# 136. Single Number
# https://leetcode.com/problems/single-number/
# Accepted: 2026-10-01T14:37:06.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 3 ms · Beats 60.78%
# Memory: 21.1 MB · Beats 45.37%
# Submission: https://leetcode.com/submissions/detail/2159290091/

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums : 
            result ^= num
        return result
