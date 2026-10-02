# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
# Accepted: 2026-10-02T15:56:27.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.2 MB · Beats 54.42%
# Submission: https://leetcode.com/submissions/detail/2160308203/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <2 : 
            return n 
        dp = [-1] * (n+1) 
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1) :
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        
