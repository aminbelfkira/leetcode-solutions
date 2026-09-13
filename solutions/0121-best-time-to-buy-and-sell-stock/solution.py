# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Accepted: 2026-09-13T21:23:43.000Z
# Language: Python3
# Runtime: 59 ms · Beats 33.52%
# Memory: 29.2 MB · Beats 7.68%
# Submission: https://leetcode.com/submissions/detail/2141025286/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for price in prices[1:] : 
            min_price = min(price, min_price)
            max_profit = max(price - min_price, max_profit)
        
        return max_profit
