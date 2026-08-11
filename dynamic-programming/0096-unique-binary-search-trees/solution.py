# 96. Unique Binary Search Trees
# https://leetcode.com/problems/unique-binary-search-trees/
# Accepted: 2026-08-11T16:30:54.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 58%
# Submission: https://leetcode.com/submissions/detail/2103126527/

class Solution:
    def numTrees(self, n: int) -> int:
        
        dp = [0] * (n+1)
        dp[0] = 1
        for k in range(1,n+1) :
            for i in range(1, k+1) : 
                dp[k] += dp[i-1] * dp[ k-i]
        return dp[n] 
