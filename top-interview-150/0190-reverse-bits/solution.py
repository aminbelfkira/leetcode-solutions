# 190. Reverse Bits
# https://leetcode.com/problems/reverse-bits/
# Accepted: 2026-10-02T18:22:48.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.1 MB · Beats 68.97%
# Submission: https://leetcode.com/submissions/detail/2160461816/

class Solution:
    def reverseBits(self, n: int) -> int:
        return int(format(n, "032b")[::-1], 2)
