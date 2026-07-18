# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Accepted: 2026-07-18T20:17:40.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 51 ms · Beats 51.68%
# Memory: 28.5 MB · Beats 75.22%
# Submission: https://leetcode.com/submissions/detail/2072776853/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = float(inf)
        max_profit = 0

        for price in prices : 

            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit
            
