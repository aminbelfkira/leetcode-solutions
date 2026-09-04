# 274. H-Index
# https://leetcode.com/problems/h-index/
# Accepted: 2026-09-04T12:32:16.000Z
# Language: Python3
# Runtime: 76 ms · Beats 6.63%
# Memory: 19.3 MB · Beats 65.87%
# Submission: https://leetcode.com/submissions/detail/2130686139/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        def aux(h) : 
            return len([c for c in citations if c >= h]) >= h
        
        h = 0
        n = len(citations)
        while h < n and aux(h+1) : 
            h+=1
        return h
