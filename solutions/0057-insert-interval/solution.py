# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/
# Accepted: 2026-09-11T17:09:03.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 21.2 MB · Beats 89.25%
# Submission: https://leetcode.com/submissions/detail/2138787746/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        ### on insert tout ceux avant 
        new_start, new_end = newInterval
        k = 0
        res = []
        while k <n and intervals[k][1] < new_start :
            res.append(intervals[k])
            k+=1
        start = new_start
        end = new_end
        while k< n and intervals[k][0] <= new_end : 
            start = min(start, intervals[k][0])
            end  = max(end, intervals[k][1])
            k+=1
        res.append([start, end])

        while k < n : 
            res.append(intervals[k])
            k+=1
        
        return res
