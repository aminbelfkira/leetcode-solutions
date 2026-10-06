# 190. Reverse Bits
# https://leetcode.com/problems/reverse-bits/
# Accepted: 2026-10-06T12:35:57.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 13.4%
# Submission: https://leetcode.com/submissions/detail/2164218458/

class Solution:
    def reverseBits(self, n: int) -> int:
        return int(format(n, "032b")[::-1], 2)
