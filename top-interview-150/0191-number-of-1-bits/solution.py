# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/
# Accepted: 2026-10-01T14:32:34.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.5 MB · Beats 5.57%
# Submission: https://leetcode.com/submissions/detail/2159286074/

class Solution:
    def hammingWeight(self, n: int) -> int:
        k = 0 
        while n : 
            k+= n%2
            n//=2
        return k 
