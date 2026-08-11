# 72. Edit Distance
# https://leetcode.com/problems/edit-distance/
# Accepted: 2026-08-11T16:15:18.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 51 ms · Beats 46.4%
# Memory: 22.6 MB · Beats 79.72%
# Submission: https://leetcode.com/submissions/detail/2103102188/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        ###dp[i][j] : word distance between word[:i] word[j]

        m = len(word1)
        n = len(word2)

        dp = [[0]*(n+1) for _ in range(m+1)]
        ##dp[i][0] = i
        ##dp [0][j] = j
        ### dp[i: j] = dp[i-1 : j-1] if dp[i-1] == dp[j-1]
        ###                     = dp[]

        for i in range(m+1) : 
            dp[i][0] = i
        for j in range(n+1) : 
            dp[0][j] = j

        for i in range(1,m+1) :
            for j in range(1,n+1) : 

                if word1[i-1] == word2[j-1] : 
                    dp[i][j] = dp[i-1][j-1]

                else : 
                    dp[i][j] = 1+ min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

        return dp[m][n] 


