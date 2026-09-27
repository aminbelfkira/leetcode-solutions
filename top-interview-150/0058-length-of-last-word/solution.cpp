// 58. Length of Last Word
// https://leetcode.com/problems/length-of-last-word/
// Accepted: 2026-09-27T15:10:13.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 0 ms · Beats 100%
// Memory: 8.8 MB · Beats 67.69%
// Submission: https://leetcode.com/submissions/detail/2155081831/

class Solution {
public:
    int lengthOfLastWord(string s) {
        int i = s.size() - 1 ; 
        while(i>=0 && s[i]== ' '){
            i-- ; 
        }
        int length = 0 ; 
        while (i>=0 && s[i] != ' '){
            length ++ ;
            i -- ;
        }
        return length ; 
    }
};
