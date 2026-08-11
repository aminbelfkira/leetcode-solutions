# 746. Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/
# Accepted: 2026-08-11T00:16:40.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 3 ms · Beats 60.67%
# Memory: 19.5 MB · Beats 25.38%
# Submission: https://leetcode.com/submissions/detail/2102125920/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        if n <=2 : 
            return min(cost)
        dp = [0] * (n+1)
        dp[1] = 0
        dp[2] = cost[2]
        for i in range(2,n+1) : 
            dp[i] = min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2])

        return dp[n] 

        
