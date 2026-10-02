# 139. Word Break
# https://leetcode.com/problems/word-break/
# Accepted: 2026-10-02T16:08:51.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 7 ms · Beats 22.92%
# Memory: 19.4 MB · Beats 53.52%
# Submission: https://leetcode.com/submissions/detail/2160319624/

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict) 
        n = len(s) 
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1, n+1) : 
            for j in range(i) :
                if dp[j] and s[j:i] in wordDict : 
                    dp[i] = True
                    break
        return dp[n]
