# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Accepted: 2026-09-11T22:15:40.000Z
# Language: Python3
# Runtime: 3 ms · Beats 60.9%
# Memory: 20.3 MB · Beats 53.68%
# Submission: https://leetcode.com/submissions/detail/2138994752/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        n = len(prices)
        for i in range(1, n) : 
            max_profit += max(prices[i] - prices[i-1], 0)
        return max_profit
        
