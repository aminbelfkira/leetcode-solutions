# 69. Sqrt(x)
# https://leetcode.com/problems/sqrtx/
# Accepted: 2026-10-01T15:08:19.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 7 ms · Beats 34.53%
# Memory: 19.3 MB · Beats 55.17%
# Submission: https://leetcode.com/submissions/detail/2159317758/

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right : 
            mid = (left + right)//2
            if mid *mid <= x : 
                left = mid +1
            else : 
                right = mid-1
        return right

