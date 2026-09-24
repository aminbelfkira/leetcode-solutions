// 27. Remove Element
// https://leetcode.com/problems/remove-element/
// Accepted: 2026-09-24T22:39:13.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 0 ms · Beats 100%
// Memory: 11.6 MB · Beats 83.91%
// Submission: https://leetcode.com/submissions/detail/2152468640/

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0 ;
        for (int i = 0; i<nums.size() ; i++){
            if (nums[i]!=val){
                nums[k] = nums[i] ; 
                k++;
            }
        }
        return k ;
    }
};
