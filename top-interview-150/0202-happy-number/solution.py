# 202. Happy Number
# https://leetcode.com/problems/happy-number/
# Accepted: 2026-09-05T16:50:14.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.1 MB · Beats 98.58%
# Submission: https://leetcode.com/submissions/detail/2131946114/

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n !=1: 
            n = sum([int(digit) **2 for digit in str(n)])
            if n in seen : 
                return False
            seen.add(n)
        return True
