# 279. Perfect Squares
# https://leetcode.com/problems/perfect-squares/
# Accepted: 2026-08-11T20:12:20.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 2234 ms · Beats 22.74%
# Memory: 39 MB · Beats 10.67%
# Submission: https://leetcode.com/submissions/detail/2103409254/

class Solution:
    def numSquares(self, n: int) -> int:
        import math
        perfect = [i**2 for i in range(1, int(math.isqrt(n)) + 1)]
        from functools import lru_cache
        
        @lru_cache(maxsize = None)
        def aux(amount) : 
            if amount ==0 : 
                return 0
            current_max = float('inf')
            for square in perfect : 
                if square >amount :
                    break
                current_max = min(current_max, aux(amount-square)+1)
            return current_max
        
        return aux(n)

