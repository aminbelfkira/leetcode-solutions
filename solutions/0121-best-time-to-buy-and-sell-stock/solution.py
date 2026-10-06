# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Accepted: 2026-10-06T12:51:37.000Z
# Language: Python3
# Runtime: 51 ms · Beats 52.05%
# Memory: 28.9 MB · Beats 10.54%
# Submission: https://leetcode.com/submissions/detail/2164231149/

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:] :
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
