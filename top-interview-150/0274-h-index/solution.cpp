// 274. H-Index
// https://leetcode.com/problems/h-index/
// Accepted: 2026-09-27T13:07:45.000Z
// Language: C++
// Collection: top-interview-150
// Runtime: 4 ms · Beats 10.07%
// Memory: 12.3 MB · Beats 64.39%
// Submission: https://leetcode.com/submissions/detail/2154975719/

class Solution {
public:
    int aux(vector<int>& citations, int h){
        int compteur = 0 ;
        for(int citation : citations){
            if(citation >= h){
                compteur++ ; 
            }
        }
        return compteur ;
    }
    int hIndex(vector<int>& citations) {

        int h = 0 ;
        while ((h< citations.size())&& (aux(citations, h+1)>= h+1)) {
            h++ ;
        }
        return h ; 
    }
};
