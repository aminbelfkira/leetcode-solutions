# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/
# Accepted: 2026-09-21T13:21:29.000Z
# Language: Python3
# Runtime: 15 ms · Beats 21.02%
# Memory: 19.6 MB · Beats 35.33%
# Submission: https://leetcode.com/submissions/detail/2148665602/

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        
        current = []
        res = []

        def aux(index) :
            if sum(current) == target : 
                res.append(current.copy())
                return
            if sum(current) > target : 
                return
            for i in range(index, len(candidates)) : 
                current.append(candidates[i])
                aux(i)
                current.pop()
        aux(0)
        return res
