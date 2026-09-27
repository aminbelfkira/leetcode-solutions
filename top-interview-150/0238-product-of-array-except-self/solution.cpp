// 238. Product of Array Except Self
// https://leetcode.com/problems/product-of-array-except-self/
// Accepted: 2026-09-27T13:55:18.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 1 ms · Beats 49.66%
// Memory: 40.1 MB · Beats 95.4%
// Submission: https://leetcode.com/submissions/detail/2155016948/

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        const int n = nums.size() ; 
        vector<int> answer(n,1) ; 

        int prefix = 1 ; 
        for (int i = 0 ; i< n ; i++){
            answer[i] *= prefix ; 
            prefix *= nums[i] ; 
        }
        int suffix = 1 ; 
        for(int i = n-1 ; i >=0 ; i--){
            answer[i] *= suffix ; 
            suffix *= nums[i] ; 
        }

        return answer ; 

    }
};
