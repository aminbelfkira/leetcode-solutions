# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/
# Accepted: 2026-10-01T15:16:46.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 97.92%
# Submission: https://leetcode.com/submissions/detail/2159325070/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 : 
            return 1
        if n < 0 :
            return 1/self.myPow(x, -n)
        a = self.myPow(x, n//2)
        if n %2 == 0 : 
            return a *a
        else : 
            return a *a *x
            
