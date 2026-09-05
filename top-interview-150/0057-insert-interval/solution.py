# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/
# Accepted: 2026-09-05T22:04:58.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 21.3 MB · Beats 89.36%
# Submission: https://leetcode.com/submissions/detail/2132182994/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        ###tous les intervals avant le premier à insérer
        results = []
        new_start = newInterval[0]
        new_end = newInterval[1]

        k = 0
        n = len(intervals)
        while k <n and intervals[k][1] < new_start : 
            results.append(intervals[k])
            k+=1
        
        ## on ajoute tous les intervalles qui sont compris dans le nouveau
        while k <n and intervals[k][0] <= new_end : 
            new_start = min(intervals[k][0], new_start)
            new_end = max(intervals[k][1], new_end)
            k+=1
        results.append([new_start, new_end])

        while k < n :
            results.append(intervals[k])
            k+=1
        return results 
