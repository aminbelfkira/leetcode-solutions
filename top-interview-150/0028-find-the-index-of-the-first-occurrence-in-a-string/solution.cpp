// 28. Find the Index of the First Occurrence in a String
// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
// Accepted: 2026-09-27T15:30:46.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 0 ms · Beats 100%
// Memory: 9.2 MB · Beats 45.89%
// Submission: https://leetcode.com/submissions/detail/2155099233/

class Solution {
public:
    int strStr(string haystack, string needle) {
        const size_t pos = haystack.find(needle) ; 

        if (pos == string::npos){
            return -1 ;
        }
        return static_cast<int>(pos) ;
    }
};
