# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/
# Accepted: 2026-09-21T07:38:28.000Z
# Language: Python3
# Runtime: 3 ms · Beats 30.12%
# Memory: 21.3 MB · Beats 58.46%
# Submission: https://leetcode.com/submissions/detail/2148404124/

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        ##on commence par les intervalles avatn celui à insérer

        new_start, new_end = newInterval
        k = 0
        res = []
        while k<len(intervals) and intervals[k][1] < new_start : 
            res.append(intervals[k])
            k+=1
        
        while k < len(intervals) and  intervals[k][0] <= new_end : 
            new_start = min(new_start, intervals[k][0])
            new_end = max(new_end, intervals[k][1])
            k+=1
        res.append([new_start, new_end])

        while k < len(intervals) :
            res.append(intervals[k])
            k+=1
        return res
        
