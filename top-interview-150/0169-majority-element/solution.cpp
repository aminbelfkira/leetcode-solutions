// 169. Majority Element
// https://leetcode.com/problems/majority-element/
// Accepted: 2026-09-24T22:49:33.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 0 ms · Beats 100%
// Memory: 42.1 MB · Beats 7.09%
// Submission: https://leetcode.com/submissions/detail/2152471370/

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int counter = 1 ;
        int majority = nums[0] ; 
        for (int i = 1 ; i< nums.size(); i++){
            if (nums[i] == majority){
                counter +=1 ; 
            } else {
                counter -=1 ;
            }
            if (counter < 0){
                counter = 1;
                majority = nums[i];
            }
        }
        return majority ; 
    }
};
