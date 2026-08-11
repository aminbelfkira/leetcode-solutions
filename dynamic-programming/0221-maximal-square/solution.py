# 221. Maximal Square
# https://leetcode.com/problems/maximal-square/
# Accepted: 2026-08-11T19:27:19.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 77 ms · Beats 76.61%
# Memory: 33 MB · Beats 79.01%
# Submission: https://leetcode.com/submissions/detail/2103375648/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        ##dp[i][j] : carré de coté j qui est commence en i
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] *n for _ in range(m)]
        max_side = 0

        for i in range(m) : 
            for j in range(n) : 
                if matrix[i][j] =="1":
                    if i == 0 or j == 0 :
                        dp[i][j] =1
                    else : 
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    max_side = max(max_side, dp[i][j])
        return max_side * max_side
