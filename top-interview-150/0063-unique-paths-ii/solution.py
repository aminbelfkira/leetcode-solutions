# 63. Unique Paths II
# https://leetcode.com/problems/unique-paths-ii/
# Accepted: 2026-10-02T18:53:24.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 33.52%
# Submission: https://leetcode.com/submissions/detail/2160488801/

class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m) : 
            for j in range(n) : 
                if grid[i][j] == 1 :
                    dp[i][j] = 0
                    continue
                
                if i == 0 and j == 0 : 
                    dp[i][j] =1
                elif i == 0 : 
                    dp[i][j] =dp[i][j-1]
                elif j == 0 : 
                    dp[i][j] = dp[i-1][j]
                else : 
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

