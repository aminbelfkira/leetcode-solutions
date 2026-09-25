// 45. Jump Game II
// https://leetcode.com/problems/jump-game-ii/
// Accepted: 2026-09-25T06:28:44.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 0 ms · Beats 100%
// Memory: 20.6 MB · Beats 78%
// Submission: https://leetcode.com/submissions/detail/2152705700/

class Solution {
public:
    int jump(vector<int>& nums) {
        int portee = nums[0] ; 
        int current_end = 0 ; 
        int jumps = 0 ; 
        for (int i = 0 ;  i< nums.size() -1; i++){
            portee = max(portee, i + nums[i]) ; 
            if (current_end == i){
                jumps +=1 ; 
                current_end = portee ; 
            }
        }
        return jumps ;
    }
};
