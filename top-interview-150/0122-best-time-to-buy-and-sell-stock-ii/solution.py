# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Accepted: 2026-09-01T18:16:40.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 3 ms · Beats 61.14%
# Memory: 20.2 MB · Beats 86.08%
# Submission: https://leetcode.com/submissions/detail/2127620351/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for i in range(1, len(prices))  : 
            profit += max(0, prices[i] - prices[i-1])
        
        return profit
