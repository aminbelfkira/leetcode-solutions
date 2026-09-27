// 125. Valid Palindrome
// https://leetcode.com/problems/valid-palindrome/
// Accepted: 2026-09-27T16:03:59.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 1 ms · Beats 42.65%
// Memory: 9.8 MB · Beats 76.68%
// Submission: https://leetcode.com/submissions/detail/2155128361/

class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0 ;
        int right = static_cast<int>(s.size()) -1 ;

        while (left < right){
            if(!isalnum(static_cast<unsigned char>(s[left]))){
                ++left ; 
            } else if (!isalnum(static_cast<unsigned char> (s[right]))){
                --right ; 
            } else {
                const auto a = static_cast<unsigned char>(s[left]) ; 
                const auto b = static_cast<unsigned char>(s[right]) ;
                if(tolower(a)!= tolower(b)){
                    return false ; 
                }
                ++left ; 
                --right ;
            }
        }
        return true ; 
    }
};
