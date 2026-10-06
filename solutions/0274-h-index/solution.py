# 274. H-Index
# https://leetcode.com/problems/h-index/
# Accepted: 2026-10-06T14:09:26.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 92.01%
# Submission: https://leetcode.com/submissions/detail/2164306953/

class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse = True)
        print(citations)

        h = 0 
        while h< len(citations) and citations[h] > h : 
            h+=1
        return h
