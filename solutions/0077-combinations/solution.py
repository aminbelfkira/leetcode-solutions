# 77. Combinations
# https://leetcode.com/problems/combinations/
# Accepted: 2026-09-21T13:14:33.000Z
# Language: Python3
# Runtime: 111 ms · Beats 46.05%
# Memory: 61.2 MB · Beats 85.75%
# Submission: https://leetcode.com/submissions/detail/2148659162/

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        current = []
        res = []

        def aux(start) : 
            if len(current) == k :
                res.append(current.copy())
                return
            for i in range(start, n+1) : 
                current.append(i)
                aux(i+1)
                current.pop()
        aux(1)
        return res
