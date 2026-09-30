# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/
# Accepted: 2026-09-30T21:52:50.000Z
# Language: Python3
# Runtime: 7 ms · Beats 73.75%
# Memory: 23.4 MB · Beats 8.33%
# Submission: https://leetcode.com/submissions/detail/2158616700/

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x : x[0])
        new_res = [intervals[0]]

        for start, end in intervals[1:] : 
            last_end = new_res[-1][1]
            if start > last_end : 
                new_res.append([start, end])
            else : 
                new_res[-1][1] = max(end, last_end)
        
        return new_res
