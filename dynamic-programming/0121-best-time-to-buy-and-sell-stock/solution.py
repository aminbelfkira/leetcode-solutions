# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Accepted: 2026-08-10T23:37:35.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 50 ms · Beats 52.56%
# Memory: 28.8 MB · Beats 10.97%
# Submission: https://leetcode.com/submissions/detail/2102113846/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = float('inf')
        max_profit = 0

        for price in prices : 
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit
