# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/
# Accepted: 2026-09-14T21:13:51.000Z
# Language: Python3
# Runtime: 16 ms · Beats 13.11%
# Memory: 19.6 MB · Beats 65.62%
# Submission: https://leetcode.com/submissions/detail/2142007311/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        result = []

        def backtrack(start) : 
            if sum(path) == target : 
                result.append(path.copy())
                return
            if sum(path) > target : 
                return
            for i in range(start, len(candidates)) : 
                path.append(candidates[i])
                backtrack(i)
                path.pop()
        backtrack(0)
        return result
