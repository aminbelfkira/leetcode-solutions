# 77. Combinations
# https://leetcode.com/problems/combinations/
# Accepted: 2026-09-13T16:38:33.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 75 ms · Beats 92.35%
# Memory: 61.3 MB · Beats 85.36%
# Submission: https://leetcode.com/submissions/detail/2140804428/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        result = []
        path = []

        def backtrack(start ) : 
            if len(path) == k :
                result.append(path.copy())
                return
            needed = k - len(path)

            for number in range(start, n- needed +2) :
                path.append(number)
                backtrack(number +1)
                path.pop()
        backtrack(1)
        return result
