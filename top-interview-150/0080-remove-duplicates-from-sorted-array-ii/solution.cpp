// 80. Remove Duplicates from Sorted Array II
// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
// Accepted: 2026-09-24T22:47:06.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 0 ms · Beats 100%
// Memory: 19.6 MB · Beats 23.89%
// Submission: https://leetcode.com/submissions/detail/2152470734/

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() <3){
            return nums.size() ;
        }
        int k = 2 ; 
        for (int i = 2; i< nums.size() ; i++){
            if (nums[i] != nums[k-2]){
                nums[k] = nums[i] ; 
                k++ ; 
            }
        }
        return k ;
    }
};
