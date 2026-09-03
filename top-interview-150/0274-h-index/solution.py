# 274. H-Index
# https://leetcode.com/problems/h-index/
# Accepted: 2026-09-03T10:45:24.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 68 ms · Beats 6.64%
# Memory: 19.4 MB · Beats 65.56%
# Submission: https://leetcode.com/submissions/detail/2129512928/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def aux(citations, k) : 

            return len([c for c in citations if c>= k]) >=k

        h = 0
        while h < len(citations) and aux(citations, h+1) : 
            h+=1
        
        return h
