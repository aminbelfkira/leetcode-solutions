// 15. 3Sum
// https://leetcode.com/problems/3sum/
// Accepted: 2026-09-27T16:34:57.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 35 ms · Beats 98.86%
// Memory: 29.1 MB · Beats 45.46%
// Submission: https://leetcode.com/submissions/detail/2155157612/

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end()) ;
        vector<vector<int>> result ;
        for (int i = 0 ; i < static_cast<int>(nums.size())-2; i++){
            if (i>0 && nums[i] == nums[i-1]){
                continue ;
            }
            if (nums[i] >0){
                break ;
            }
            int left = i +1; 
            int right = static_cast<int>(nums.size()) -1 ; 
            const int target = -nums[i] ; 
            while (left < right){
                const int sum = nums[left] + nums[right] ; 
                if (sum == target){
                    result.push_back({nums[i], nums[left], nums[right]}) ;
                    ++left ; 
                    --right ;;
                    while (left < right && nums[left]==nums[left -1]){
                        ++left ;
                    }
                    while (left < right && nums[right]==nums[right +1]){
                        --right ;
                    }
                } else if (sum>target) {
                    --right ;
                } else {
                    ++ left ;
                }
            }
        } 
        return result ;
    }
};
