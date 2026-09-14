# 77. Combinations
# https://leetcode.com/problems/combinations/
# Accepted: 2026-09-14T20:46:18.000Z
# Language: Python3
# Runtime: 182 ms · Beats 9.93%
# Memory: 61.3 MB · Beats 85.44%
# Submission: https://leetcode.com/submissions/detail/2141995583/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path =[]
        result = []

        def backtrack(start) : 
            if len(path) == k :
                result.append(path.copy())
            for i in range(start, n+1) :
                path.append(i)
                backtrack(i+1)
                path.pop()
        backtrack(1)
        return result
