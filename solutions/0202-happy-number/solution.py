# 202. Happy Number
# https://leetcode.com/problems/happy-number/
# Accepted: 2026-09-11T21:28:14.000Z
# Language: Python3
# Runtime: 3 ms · Beats 33.73%
# Memory: 19.3 MB · Beats 62.46%
# Submission: https://leetcode.com/submissions/detail/2138979595/

class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        while n != 1 : 
            digits = str(n)
            n = sum([int(d)**2 for d in digits])
            if n in seen : 
                return False
            seen.add(n)
        return True
