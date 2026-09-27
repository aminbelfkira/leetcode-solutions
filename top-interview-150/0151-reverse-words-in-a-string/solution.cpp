// 151. Reverse Words in a String
// https://leetcode.com/problems/reverse-words-in-a-string/
// Accepted: 2026-09-27T15:21:47.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 0 ms · Beats 100%
// Memory: 10.1 MB · Beats 79.54%
// Submission: https://leetcode.com/submissions/detail/2155091513/

class Solution {
public:
    string reverseWords(string s) {
        string result ; 
        result.reserve(s.size()) ; 

        size_t pos = s.size() ; 
        while (pos>0) {
            while (pos >0 && s[pos -1] == ' '){
                --pos ; 
            }
            const size_t end = pos ; 
            while (pos>0 && s[pos -1] != ' '){
                --pos ;
            }
            if (pos == end) {
                break ;
            }
            if (!result.empty()){
                result+=' ';
            }
            result.append(s, pos, end-pos) ; 
        }
        return result ;
    }
};
