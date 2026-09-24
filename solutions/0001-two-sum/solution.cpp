// 1. Two Sum
// https://leetcode.com/problems/two-sum/
// Accepted: 2026-09-24T20:32:18.000Z
// Language: C++
// Runtime: 3 ms · Beats 67.86%
// Memory: 15.4 MB · Beats 7.73%
// Submission: https://leetcode.com/submissions/detail/2152424213/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen ; 
        seen.reserve(nums.size()) ; 
        for (int i=0 ; i< static_cast<int>(nums.size()) ; i++) {
            if (auto it = seen.find(target - nums[i]); it!= seen.end()){
                return {it->second, i} ;
            }
            seen.emplace(nums[i],i);
        }
        return {} ;
    }
};
