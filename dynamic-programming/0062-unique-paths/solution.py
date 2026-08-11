# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/
# Accepted: 2026-08-11T15:18:09.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 21.61%
# Submission: https://leetcode.com/submissions/detail/2103022787/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp =[[0] * n for _ in range(m)]

        for i in range(m) : 
            for j in range(n) : 
                
                if i ==0 and j == 0 : 
                    dp[0][0] = 1
                elif i ==0 : 
                    dp[0][j] = dp[0][j-1]
                elif j == 0 : 
                    dp[i][0] = dp[i-1][0]
                else : 
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
        return dp[m-1][n-1]
        
