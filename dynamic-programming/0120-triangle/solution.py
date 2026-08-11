# 120. Triangle
# https://leetcode.com/problems/triangle/
# Accepted: 2026-08-11T16:51:10.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 3 ms · Beats 70.12%
# Memory: 20 MB · Beats 62.9%
# Submission: https://leetcode.com/submissions/detail/2103158871/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp =triangle[-1][:]
        n = len(triangle)
        for i in range(n-2, -1, -1) : 
            for j in range(len(triangle[i])) :
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        return dp[0]


