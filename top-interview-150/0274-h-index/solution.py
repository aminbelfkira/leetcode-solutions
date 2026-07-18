# 274. H-Index
# https://leetcode.com/problems/h-index/
# Accepted: 2026-07-18T21:55:17.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 67 ms · Beats 6.25%
# Memory: 19.3 MB · Beats 64.25%
# Submission: https://leetcode.com/submissions/detail/2072817634/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def aux(citations, h) : 
            return len([c for c in citations if c >=h]) >= h 
        
        k = 0
        while k<len(citations) and aux(citations, k+1) : 
            k +=1
    
        return k
