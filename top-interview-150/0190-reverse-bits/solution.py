# 190. Reverse Bits
# https://leetcode.com/problems/reverse-bits/
# Accepted: 2026-10-02T18:20:54.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 3 ms · Beats 84.93%
# Memory: 19.2 MB · Beats 68.97%
# Submission: https://leetcode.com/submissions/detail/2160459769/

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result
