// 3. Longest Substring Without Repeating Characters
// https://leetcode.com/problems/longest-substring-without-repeating-characters/
// Accepted: 2026-09-27T17:10:08.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 49 ms · Beats 59.1%
// Memory: 19.3 MB · Beats 47.17%
// Submission: https://leetcode.com/submissions/detail/2155194475/

#include <unordered_map>
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> last_seen ;
        int left = 0 ; 
        int best = 0 ;
        for (int right = 0 ; right <static_cast<int>(s.size()); ++ right){
            const auto it = last_seen.find(s[right]) ;
            if (it != last_seen.end() && it->second >= left){
                left = it-> second +1 ; 
            }
            last_seen[s[right]] = right ;
            best = max(best, right - left +1) ; 
        }
        return best ;
    }
};
