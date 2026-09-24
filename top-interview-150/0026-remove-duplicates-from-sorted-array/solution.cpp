// 26. Remove Duplicates from Sorted Array
// https://leetcode.com/problems/remove-duplicates-from-sorted-array/
// Accepted: 2026-09-24T22:43:22.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 0 ms · Beats 100%
// Memory: 22.8 MB · Beats 18.15%
// Submission: https://leetcode.com/submissions/detail/2152469736/

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()){
            return 0 ;
        }
        int k = 1 ; 
        for (int i = 1 ; i<nums.size(); i++){
            if (nums[i] != nums[i-1]){
                nums[k] = nums[i] ; 
                k++;
            }
        }
        return k ;
    }
};
