// 392. Is Subsequence
// https://leetcode.com/problems/is-subsequence/
// Accepted: 2026-09-27T16:07:05.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 0 ms · Beats 100%
// Memory: 8.6 MB · Beats 31.56%
// Submission: https://leetcode.com/submissions/detail/2155131109/

class Solution {
public:
    bool isSubsequence(string s, string t) {
        size_t i = 0 ;
        for (char c : t){
            if (i<s.size() && s[i]== c){
                ++i ;
            }
        }
        return i == s.size() ;
    }
};
