// 121. Best Time to Buy and Sell Stock
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
// Accepted: 2026-09-24T23:00:29.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 0 ms · Beats 100%
// Memory: 97.3 MB · Beats 61.91%
// Submission: https://leetcode.com/submissions/detail/2152474133/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0 ; 
        int min_price = prices[0] ; 
        for (int i = 1 ; i< prices.size() ; i ++){
            min_price = min(min_price, prices[i]) ; 
            profit = max(profit, prices[i] - min_price) ;
        }
        return profit ; 
    }
};
