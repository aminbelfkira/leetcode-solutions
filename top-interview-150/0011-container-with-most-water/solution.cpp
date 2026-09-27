// 11. Container With Most Water
// https://leetcode.com/problems/container-with-most-water/
// Accepted: 2026-09-27T16:18:15.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 4 ms · Beats 20.48%
// Memory: 62.9 MB · Beats 78.87%
// Submission: https://leetcode.com/submissions/detail/2155141438/

class Solution {
public:
    int maxArea(vector<int>& height) {
        int max_area = 0 ;
        int left = 0 ;
        int right = static_cast<int>(height.size()) - 1 ;
        
        while (left < right){
            const int area = min(height[right], height[left]) * (right-left) ;
            max_area = max(area, max_area) ; 
            if (height[left] > height[right]){
                --right ; 
            } else {
                ++ left ; 
            }
        }
        return max_area ; 
    }
};
