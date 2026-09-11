# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/
# Accepted: 2026-09-11T22:19:50.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 29.31%
# Submission: https://leetcode.com/submissions/detail/2138995938/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m, n = len(matrix) , len(matrix[0])
        for i in range(m) : 
            for j in range(i) : 
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(m) : 
            matrix[i][:] = matrix[i][::-1]
