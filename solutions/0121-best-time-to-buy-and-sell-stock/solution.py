# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Accepted: 2026-09-03T20:33:05.000Z
# Language: Python3
# Runtime: 47 ms · Beats 59.1%
# Memory: 28.8 MB · Beats 11.42%
# Submission: https://leetcode.com/submissions/detail/2130082466/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        min_price = float('inf')

        for price in prices : 
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit
