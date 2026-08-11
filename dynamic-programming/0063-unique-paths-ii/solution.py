# 63. Unique Paths II
# https://leetcode.com/problems/unique-paths-ii/
# Accepted: 2026-08-11T15:39:55.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 0 ms · Beats 100%
# Memory: 19.5 MB · Beats 31.17%
# Submission: https://leetcode.com/submissions/detail/2103051883/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1- obstacleGrid[0][0]

        for i in range(m) : 
            for j in range(n) : 
                if i == 0 and j == 0 : 
                    continue
                elif obstacleGrid[i][j] :
                    dp[i][j] = 0
                else : 
                    up = dp[i-1][j] if i > 0 else 0
                    left = dp[i][j-1] if j > 0 else 0
                    dp[i][j] = up + left
        return dp[m-1][n-1]
