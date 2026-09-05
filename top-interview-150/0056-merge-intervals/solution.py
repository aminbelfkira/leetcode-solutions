# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/
# Accepted: 2026-09-05T21:52:46.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 4 ms · Beats 84.44%
# Memory: 23.1 MB · Beats 39.61%
# Submission: https://leetcode.com/submissions/detail/2132178874/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x :x[0])
        results = [intervals[0]]

        for start, end in intervals[1:] : 
            last_end= results[-1][1]
            if start <= last_end : 
                results[-1][1] = max(last_end, end)
            else :
                results.append([start, end])
            
        return results
