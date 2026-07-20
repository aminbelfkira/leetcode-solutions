# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/
# Accepted: 2026-07-20T22:19:28.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.1 MB · Beats 92.65%
# Submission: https://leetcode.com/submissions/detail/2075114525/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)

        for i in range(n) : 
            for j in range(i+1, n) : 
                matrix[i][j], matrix[j][i] =  matrix[j][i] , matrix[i][j]
            
        for i in range(n) : 
            matrix[i] = matrix[i][::-1]
