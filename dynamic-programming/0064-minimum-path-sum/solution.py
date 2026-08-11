# 64. Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/
# Accepted: 2026-08-11T15:46:19.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 7 ms · Beats 92.04%
# Memory: 21.6 MB · Beats 58.82%
# Submission: https://leetcode.com/submissions/detail/2103060710/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0]*n for _ in range(m)] 

        dp[0][0] = grid[0][0]

        for i in range(m) : 
            for j in range(n) : 
                if i == 0 and j == 0 : 
                    continue
                up = dp[i-1][j] if i>0 else float('inf')
                left = dp[i][j-1] if j>0 else float('inf')
                dp[i][j] = min(up, left) + grid[i][j]
            
        return dp[m-1][n-1]
        
