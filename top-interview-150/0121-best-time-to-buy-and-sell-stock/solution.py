# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Accepted: 2026-09-01T18:15:38.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 62 ms · Beats 27.45%
# Memory: 28.6 MB · Beats 76.32%
# Submission: https://leetcode.com/submissions/detail/2127618879/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')

        for price in prices : 
            min_price = min(price, min_price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit
