# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/
# Accepted: 2026-09-04T13:06:50.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.2 MB · Beats 93.01%
# Submission: https://leetcode.com/submissions/detail/2130715727/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m) : 
            for j in range(i) : 

                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(m) : 
            matrix[i][:] = matrix[i][::-1]
        
