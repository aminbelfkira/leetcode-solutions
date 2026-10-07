# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/
# Accepted: 2026-10-07T07:03:20.000Z
# Language: Python3
# Runtime: 1 ms · Beats 42.79%
# Memory: 21.3 MB · Beats 58.47%
# Submission: https://leetcode.com/submissions/detail/2165024602/

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        k = 0
        n = len(intervals)
        new_start, new_end = newInterval
        while k<n and new_start > intervals[k][1] : 
            res.append(intervals[k])
            k+=1
        
        while k< n and new_end >= intervals[k][0] : 
            new_start = min(new_start, intervals[k][0])
            new_end = max(new_end, intervals[k][1])
            k+=1
        res.append([new_start, new_end])
        while k < n : 
            res.append(intervals[k])
            k+=1
        return res
            
