// 14. Longest Common Prefix
// https://leetcode.com/problems/longest-common-prefix/
// Accepted: 2026-09-27T15:14:41.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 0 ms · Beats 100%
// Memory: 11.7 MB · Beats 94.33%
// Submission: https://leetcode.com/submissions/detail/2155085637/

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()){return "" ; }
        const string& first = strs[0] ; 
        for(size_t i = 0 ; i< first.size() ; i++){
            for (const string& word : strs){
                if (i == word.size() || word[i] != first[i]) {
                    return first.substr(0,i) ; 
                }
            }
        }
        return first ; 
    }
};
