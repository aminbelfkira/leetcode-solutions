# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Accepted: 2026-08-11T16:54:37.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 1 ms · Beats 72.7%
# Memory: 20.3 MB · Beats 85.56%
# Submission: https://leetcode.com/submissions/detail/2103164629/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        for i in range(1,len(prices)) : 
            max_profit += max(prices[i] - prices[i-1], 0)
        return max_profit
