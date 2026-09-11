# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/
# Accepted: 2026-09-11T17:00:45.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 23.2 MB · Beats 28.96%
# Submission: https://leetcode.com/submissions/detail/2138778829/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        res = [intervals[0]]

        for start, end in intervals[1:] : 
            last_end = res[-1][1]

            if start <= last_end :
                res[-1][1] = max(last_end, end)
            else : 
                res.append([start, end])
        
        return res 
