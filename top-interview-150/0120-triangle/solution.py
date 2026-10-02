# 120. Triangle
# https://leetcode.com/problems/triangle/
# Accepted: 2026-10-02T18:27:06.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 1 ms · Beats 79.59%
# Memory: 20 MB · Beats 64.2%
# Submission: https://leetcode.com/submissions/detail/2160466432/

class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        
        dp = triangle[-1][:]
        n = len(triangle)
        for i in range(n-2, -1, -1) : 
            for j in range(len(triangle[i])) : 
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        return dp[0]
