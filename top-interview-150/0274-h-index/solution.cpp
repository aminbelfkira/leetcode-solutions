// 274. H-Index
// https://leetcode.com/problems/h-index/
// Accepted: 2026-09-27T13:38:47.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 2 ms · Beats 16.91%
// Memory: 13.6 MB · Beats 7.55%
// Submission: https://leetcode.com/submissions/detail/2155002355/

class Solution {
public:

    int hIndex(vector<int>& citations) {

        sort(citations.rbegin(), citations.rend()) ; 
        int h = 0 ; 

        for (int i = 0 ; i < citations.size() ; i++){
            if(citations[i]>= i +1){
                h = i+1 ; 
            } else 
            break ; 
        }
        return h ; 
    }
};
