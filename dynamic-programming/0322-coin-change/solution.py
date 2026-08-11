# 322. Coin Change
# https://leetcode.com/problems/coin-change/
# Accepted: 2026-08-11T20:27:52.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 515 ms · Beats 56.3%
# Memory: 19.7 MB · Beats 38.7%
# Submission: https://leetcode.com/submissions/detail/2103418972/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')] *(amount +1)
        dp[0] = 0
        for i in range(1, amount+1) :
            for coin in coins : 
                if i-coin >= 0 : 
                    dp[i] = min(dp[i-coin] +1, dp[i])
        return dp[amount] if dp[amount] != float('inf') else -1
