# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
# Accepted: 2026-10-02T15:55:12.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.1 MB · Beats 98.08%
# Submission: https://leetcode.com/submissions/detail/2160307087/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <2 : 
            return n 
        dp = [-1] * (n+1) 
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1) :
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        
