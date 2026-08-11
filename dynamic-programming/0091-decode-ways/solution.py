# 91. Decode Ways
# https://leetcode.com/problems/decode-ways/
# Accepted: 2026-08-11T16:21:09.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 21.79%
# Submission: https://leetcode.com/submissions/detail/2103111202/

class Solution:
    from functools import lru_cache
    @lru_cache
    def numDecodings(self, s: str) -> int:
        if not s : 
            return 1
        if int(s[0]) == 0 :
            return 0
        res = 0
        if int(s[:2]) >= 10 and int(s[:2]) <27 : 
            res += self.numDecodings(s[2:])
        res += self.numDecodings(s[1:])

        return res
        
