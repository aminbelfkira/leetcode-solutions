# 64. Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/
# Accepted: 2026-10-02T18:38:00.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 7 ms · Beats 91.72%
# Memory: 21.8 MB · Beats 35.18%
# Submission: https://leetcode.com/submissions/detail/2160476527/

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0]* n for _ in range(m)]

        for i in range(m) : 
            for j in range(n) : 
                if i== 0 and j == 0 : 
                    dp[i][j] = grid[i][j]
                elif i == 0 :
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0 : 
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else :
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[m-1][n-1]
