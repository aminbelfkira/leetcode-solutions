// 6. Zigzag Conversion
// https://leetcode.com/problems/zigzag-conversion/
// Accepted: 2026-09-27T15:27:09.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 6 ms · Beats 46.26%
// Memory: 13.6 MB · Beats 83.23%
// Submission: https://leetcode.com/submissions/detail/2155096067/

class Solution {
public:
    string convert(string s, int numRows) {
        
        if (numRows ==1 || numRows >= static_cast<int>(s.size())) {
            return s ; 
        }
        vector<string> rows(numRows) ; 
        int row = 0 ; 
        int direction = 1 ; 
        for (char c : s){
            rows[row] += c ; 
            if (row == 0) {
                direction = 1 ;
            } else if (row == numRows -1){
                direction =-1 ;
            }
            row += direction ;
        } 
        string result ;
        result.reserve(s.size()) ; 
        for(const string& line : rows) {
            result += line ; 
        }
        return result ; 
    }
};
