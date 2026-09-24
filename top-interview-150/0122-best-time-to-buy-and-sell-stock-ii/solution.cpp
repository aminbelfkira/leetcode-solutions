// 122. Best Time to Buy and Sell Stock II
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
// Accepted: 2026-09-24T23:02:11.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 0 ms · Beats 100%
// Memory: 20.1 MB · Beats 62.8%
// Submission: https://leetcode.com/submissions/detail/2152474600/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0 ; 
        for (int i = 1 ; i< prices.size() ; i++){
            profit += max(0, prices[i] - prices[i-1]) ; 
        }
        return profit ;
    }
};
