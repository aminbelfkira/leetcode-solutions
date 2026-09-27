// 28. Find the Index of the First Occurrence in a String
// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
// Accepted: 2026-09-27T15:33:36.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 0 ms · Beats 100%
// Memory: 8.9 MB · Beats 99.68%
// Submission: https://leetcode.com/submissions/detail/2155101799/

class Solution {
public:
    int strStr(string haystack, string needle) {

        const int n = static_cast<int>(haystack.size()) ; 
        const int m = static_cast<int>(needle.size()) ;

        if(m==0) {
            return 0;
        }
        for (int i = 0 ; i+m <= n ; i++){
            int j = 0 ; 
            while (j< m && haystack[i+j] == needle[j]){
                ++j ;
            }
            if(j==m){
                return i;
            }
        }
        return -1 ; 
    }
};
