// 55. Jump Game
// https://leetcode.com/problems/jump-game/
// Accepted: 2026-09-25T06:22:38.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 0 ms · Beats 100%
// Memory: 52.5 MB · Beats 25.82%
// Submission: https://leetcode.com/submissions/detail/2152699954/

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int portee = 0 ; 
        for (int i = 0 ; i< nums.size() ; i++){
            if(i > portee){
                return false ; 
            }
            portee = max(portee, i+ nums[i]) ;
        }
    return portee >=nums.size()-1 ; 
    }
};
