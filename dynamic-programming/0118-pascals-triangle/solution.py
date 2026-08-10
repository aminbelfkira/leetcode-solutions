# 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/
# Accepted: 2026-08-10T23:34:25.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 68.35%
# Submission: https://leetcode.com/submissions/detail/2102112945/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        current = [1]
        for i in range(numRows-1) :
            new = [1]*(len(current)+1)
            for j in range(1, len(current)) : 
                new[j] = current[j] + current[j-1]
            res.append(new)
            current = new.copy()
        return res
            
                
