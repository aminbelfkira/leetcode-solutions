// 134. Gas Station
// https://leetcode.com/problems/gas-station/
// Accepted: 2026-09-27T14:01:43.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 0 ms · Beats 100%
// Memory: 112.6 MB · Beats 23.78%
// Submission: https://leetcode.com/submissions/detail/2155022701/

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int tank = 0 ;
        int total = 0 ;
        int start = 0 ;
        for(int i = 0 ; i < gas.size() ; i++){
            const int diff = gas[i] - cost[i] ; 
            total += diff ; 
            tank += diff ; 
            if (tank  <0){
                start = i +1 ;
                tank = 0 ; 
            } 
        }
        if (total >= 0){
            return start ; 
        } else {
            return -1 ;
        }
    
    }
};
