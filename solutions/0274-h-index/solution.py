# 274. H-Index
# https://leetcode.com/problems/h-index/
# Accepted: 2026-09-11T21:24:03.000Z
# Language: Python3
# Runtime: 71 ms · Beats 6.64%
# Memory: 19.3 MB · Beats 65.53%
# Submission: https://leetcode.com/submissions/detail/2138978077/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def aux(citations, k) : 
            return len([c for c in citations if c >= k ]) >= k
        
        h = 0 
        n = len(citations)
        while h<n and aux(citations, h+1) : 
            h+=1
        
        return h
