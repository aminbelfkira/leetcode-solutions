# 172. Factorial Trailing Zeroes
# https://leetcode.com/problems/factorial-trailing-zeroes/
# Accepted: 2026-10-01T15:01:36.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.2 MB · Beats 64.13%
# Submission: https://leetcode.com/submissions/detail/2159311909/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n>= 5:
            n//= 5 
            count +=n
        return count
