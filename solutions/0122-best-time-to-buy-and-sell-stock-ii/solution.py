# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Accepted: 2026-07-20T22:39:38.000Z
# Language: Python3
# Runtime: 3 ms · Beats 61.02%
# Memory: 20.4 MB · Beats 20.25%
# Submission: https://leetcode.com/submissions/detail/2075120404/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        for i in range(1,len(prices)) : 
            max_profit = max_profit +  max(0, prices[i] - prices[i-1])
        return max_profit
