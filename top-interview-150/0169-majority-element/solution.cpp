// 169. Majority Element
// https://leetcode.com/problems/majority-element/
// Accepted: 2026-09-24T22:52:58.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 0 ms · Beats 100%
// Memory: 41.9 MB · Beats 13.89%
// Submission: https://leetcode.com/submissions/detail/2152472201/

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = 0 ;
        int counter = 0 ; 
        for (int num : nums) {
            if (counter == 0 ){
                candidate = num;
            }
            counter += (candidate == num) ? 1 : -1 ;
        }
        return candidate; 
    }
};
