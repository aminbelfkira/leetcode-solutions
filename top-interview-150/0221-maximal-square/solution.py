# 221. Maximal Square
# https://leetcode.com/problems/maximal-square/
# Accepted: 2026-10-02T22:34:06.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 79 ms · Beats 70.44%
# Memory: 33.1 MB · Beats 71.14%
# Submission: https://leetcode.com/submissions/detail/2160589420/

class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m = len(matrix) 
        n = len(matrix[0])
        ##dp[i][j] = la longueur du côté du plus grand carré rempli uniquement de 1 dont la case (i,j) est le coin inférieur droit.
        dp = [[0] *n for _ in range(m)]
        max_side = 0
        for i in range(m) : 
            for j in range(n) : 
                if matrix[i][j] == "1" : 
                    if i == 0 or j == 0 :
                        dp[i][j] = 1
                    else : 
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) 
                    max_side = max(max_side, dp[i][j])
        return max_side * max_side
