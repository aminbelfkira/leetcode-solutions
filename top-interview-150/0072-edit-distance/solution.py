# 72. Edit Distance
# https://leetcode.com/problems/edit-distance/
# Accepted: 2026-10-02T22:21:26.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 51 ms · Beats 46.58%
# Memory: 22.7 MB · Beats 65.22%
# Submission: https://leetcode.com/submissions/detail/2160586017/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ##dp[i][j] : distance entre i et j 
        m = len(word1) 
        n = len(word2)

        dp = [[0]*(n+1) for _ in range(m+1)]

        ##dp[i][0] = i
        ##dp[0][j]=j
        ##dp[i][j] = dp[i-1, j-1] si word1[i]==word2[j]
        for i in range(m+1) :
            dp[i][0] = i 
        for j in range(n+1) : 
            dp[0][j] = j
        
        for i in range(1, m+1) :
            for j in range(1, n+1) : 
                if word1[i-1] == word2[j-1] :
                    dp[i][j] = dp[i-1][j-1]
                else : 
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        
        return dp[m][n]
