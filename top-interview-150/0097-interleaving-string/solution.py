# 97. Interleaving String
# https://leetcode.com/problems/interleaving-string/
# Accepted: 2026-10-02T19:22:02.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 10 ms · Beats 79.81%
# Memory: 19.3 MB · Beats 72.04%
# Submission: https://leetcode.com/submissions/detail/2160508428/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2) 
        if n+m != len(s3) :
            return False
        dp = [[0]*(n+1) for _ in range(m+1)]
        ##dp[i][j] : peut on former s3[:i+J] avec s1[:i] et s[j]
        dp[0][0] = True
        for i in range(m+1) : 
            for j in range(n+1) :
                if i == 0 and j == 0 : 
                    continue
                from_s1 = i>0 and dp[i-1][j] and s1[i-1] == s3[i+j -1]
                from_s2 = j>0 and dp[i][j-1] and s2[j-1] == s3[i+j-1]
                dp[i][j] = from_s1 or from_s2
        return dp[m][n]
