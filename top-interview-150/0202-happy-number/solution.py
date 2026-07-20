# 202. Happy Number
# https://leetcode.com/problems/happy-number/
# Accepted: 2026-07-20T23:50:50.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.1 MB · Beats 90.18%
# Submission: https://leetcode.com/submissions/detail/2075139828/

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n!=1 : 

            digits = [int(char)**2 for char in str(n)]
            n = sum(digits)
            if n in seen : 
                return False
            seen.add(n)
        
        return True
