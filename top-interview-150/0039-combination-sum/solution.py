# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/
# Accepted: 2026-09-13T16:51:00.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 27 ms · Beats 7.23%
# Memory: 19.6 MB · Beats 65.74%
# Submission: https://leetcode.com/submissions/detail/2140816874/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        current = []
        result = []
        candidates = sorted(candidates)
        def backtrack(index) : 
            if target == sum(current) : 
                result.append(current.copy())
                return
            elif sum(current)>target :
                return
            else : 
                for i in range(index, len(candidates)) : 
                    current.append(candidates[i])
                    backtrack(i)
                    current.pop()
        backtrack(0)
        return result
