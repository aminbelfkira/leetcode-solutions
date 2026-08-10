# 338. Counting Bits
# https://leetcode.com/problems/counting-bits/
# Accepted: 2026-08-10T23:42:22.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 4 ms · Beats 65.16%
# Memory: 20.2 MB · Beats 42%
# Submission: https://leetcode.com/submissions/detail/2102115271/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
