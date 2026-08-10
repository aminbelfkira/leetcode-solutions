# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
# Accepted: 2026-08-10T23:17:42.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 3051 ms · Beats 0.07%
# Memory: 19.3 MB · Beats 17.21%
# Submission: https://leetcode.com/submissions/detail/2102108324/

class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [0] *(n+1)
        
        def aux(i) : 
            if i<=2 : 
                return i
            if i in dp : 
                return dp[i]
            dp[i] = aux(i-1) + aux(i-2)    
            return dp[i]
        return aux(n)
