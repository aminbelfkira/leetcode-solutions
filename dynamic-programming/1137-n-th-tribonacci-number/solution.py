# 1137. N-th Tribonacci Number
# https://leetcode.com/problems/n-th-tribonacci-number/
# Accepted: 2026-08-11T02:01:47.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 4 ms · Beats 0.55%
# Memory: 19.3 MB · Beats 53.98%
# Submission: https://leetcode.com/submissions/detail/2102169552/

class Solution:
    def tribonacci(self, n: int) -> int:
        
        tri = [0]*(n+1)
        if n==0 :
            return 0
        if n<=2 : 
            return 1
        tri[1]= 1
        tri[2] = 1
        for i in range(2,n+1) :
            tri[i] = tri[i-1] + tri[i-2] + tri[i-3]
        
        return tri[n]
             
