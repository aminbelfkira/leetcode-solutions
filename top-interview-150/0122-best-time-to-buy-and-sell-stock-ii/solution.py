# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Accepted: 2026-07-18T20:20:35.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 3 ms · Beats 60.96%
# Memory: 20.2 MB · Beats 97.82%
# Submission: https://leetcode.com/submissions/detail/2072778427/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0

        for i in range(1, len(prices)) : 
            max_profit +=max(0, prices[i] - prices[i-1])
        
        return max_profit
