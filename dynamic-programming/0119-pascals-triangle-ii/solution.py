# 119. Pascal's Triangle II
# https://leetcode.com/problems/pascals-triangle-ii/
# Accepted: 2026-08-10T23:36:08.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 58.2%
# Submission: https://leetcode.com/submissions/detail/2102113419/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        current = [1]
        for i in range(rowIndex) :
            new = [1]*(len(current)+1)
            for j in range(1, len(current)) : 
                new[j] = current[j] + current[j-1]
            current = new.copy()
        return current
            
        
