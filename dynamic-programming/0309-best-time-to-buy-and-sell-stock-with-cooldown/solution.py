# 309. Best Time to Buy and Sell Stock with Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# Accepted: 2026-08-11T20:20:41.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 68.94%
# Submission: https://leetcode.com/submissions/detail/2103414531/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices :
            return 0
        
        held = -prices[0]
        sold = 0
        rest = 0

        for i in range(1, len(prices)) : 
            prev_held, prev_sold, prev_rest = held, sold, rest
            held = max(prev_held, prev_rest - prices[i])
            sold = prev_held + prices[i]
            rest = max(prev_rest, prev_sold)

        return max(sold, rest)
        
