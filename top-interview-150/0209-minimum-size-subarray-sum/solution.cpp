// 209. Minimum Size Subarray Sum
// https://leetcode.com/problems/minimum-size-subarray-sum/
// Accepted: 2026-09-27T16:56:53.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 0 ms · Beats 100%
// Memory: 42 MB · Beats 5.91%
// Submission: https://leetcode.com/submissions/detail/2155180200/

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int left = 0 ;
        int n = static_cast<int>(nums.size()) ; 
        int max_length = n+1 ; 
        int sum = 0 ;
        for (int right = 0; right < n ; right ++){
            sum += nums[right] ;
            while (sum >= target) {
                max_length = min(max_length, right -left +1) ;
                sum -= nums[left] ;
                ++left ; 
            }
        }
        return max_length == n+1 ? 0 : max_length ; 
    }
};
