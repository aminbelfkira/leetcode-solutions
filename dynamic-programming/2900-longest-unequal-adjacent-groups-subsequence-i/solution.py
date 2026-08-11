# 2900. Longest Unequal Adjacent Groups Subsequence I
# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/
# Accepted: 2026-08-11T02:18:12.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 0 ms · Beats 100%
# Memory: 19.2 MB · Beats 72.96%
# Submission: https://leetcode.com/submissions/detail/2102177902/

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        ### dp[i] = plus longue subsequence until s[:i]
        ## max(dp[i-1]) + 1 ifgroups[char] !groupt_last
        n = len(words)
        group_last = None
        dp = [0] * (n+1)
        if n<=1 : 
            return words
        res = []
        for i in range(1, n+1) : 

            if (group_last is None or group_last != groups[i-1]) :
                dp[i] = dp[i-1] + 1
                group_last = groups[i-1]
                res.append(words[i-1])
            else :
                dp[i] = dp[i-1]
        return res
