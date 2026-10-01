# 137. Single Number II
# https://leetcode.com/problems/single-number-ii/
# Accepted: 2026-10-01T14:43:17.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 5 ms · Beats 38.01%
# Memory: 20.5 MB · Beats 63.56%
# Submission: https://leetcode.com/submissions/detail/2159295637/

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = 0
        twos = 0

        for num in nums : 
            ones = (ones ^num) &~twos  ##bit appar une fois modulo 3
            twos = (twos^num) & ~ones ## bit apparu deux fois modulo 3
        return ones 
