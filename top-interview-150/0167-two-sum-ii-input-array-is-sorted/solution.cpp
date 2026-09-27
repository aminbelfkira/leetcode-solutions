// 167. Two Sum II - Input Array Is Sorted
// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
// Accepted: 2026-09-27T16:13:40.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 0 ms · Beats 100%
// Memory: 25.7 MB · Beats 9.15%
// Submission: https://leetcode.com/submissions/detail/2155137279/

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        size_t left = 0 ;
        size_t right = numbers.size() - 1 ; 
        while (left < right){
            const int current_sum = numbers[left] + numbers[right] ;
            if (current_sum == target){
                return vector<int>{static_cast<int>(left) +1, static_cast<int>(right) +1} ; 
            } else if (current_sum >target){
                --right ;
            } else {
                ++left ; 
            }
        }
        return {} ; 
    }
};
