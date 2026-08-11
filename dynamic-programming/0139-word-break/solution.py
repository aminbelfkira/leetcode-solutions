# 139. Word Break
# https://leetcode.com/problems/word-break/
# Accepted: 2026-08-11T18:29:53.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 9 ms · Beats 5.84%
# Memory: 19.4 MB · Beats 52.83%
# Submission: https://leetcode.com/submissions/detail/2103316296/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        word_set = set(wordDict)

        ###dp[i] : can we cut s[:i] in wordDict words ?

        n = len(s) 
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1,n+1) : 
            for j in range(i) : 
                if dp[j] and s[j:i] in wordDict : 
                    dp[i] = True
                    break
        
        return dp[n]
