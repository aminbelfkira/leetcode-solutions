# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/
# Accepted: 2026-09-30T22:11:18.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 21.3 MB · Beats 90.05%
# Submission: https://leetcode.com/submissions/detail/2158622405/

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

        res = []
        n = len(intervals)
        new_start, new_end = newInterval
        k = 0 
        ##tout ceux avant le merge
        while k <n and new_start > intervals[k][1] : 
            res.append(intervals[k])
            k+=1
        while k < n and new_end >= intervals[k][0] :
            new_end = max(new_end, intervals[k][1])
            new_start = min(new_start, intervals[k][0])
            k+=1
        res.append([new_start, new_end])

        while k < n :
            res.append(intervals[k])
            k+=1

        return res 
        

        
