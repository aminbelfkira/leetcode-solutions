// 189. Rotate Array
// https://leetcode.com/problems/rotate-array/
// Accepted: 2026-09-24T22:57:03.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 0 ms · Beats 100%
// Memory: 263.3 MB · Beats 44.98%
// Submission: https://leetcode.com/submissions/detail/2152473267/

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size() ; 
        k = k %n ; 
        std::reverse(nums.begin(), nums.end()) ; 
        std:: reverse(nums.begin(), nums.begin()+k) ;
        std::reverse(nums.begin()+k,nums.end()) ; 
    }
};
