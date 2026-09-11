# 73. Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/
# Accepted: 2026-09-11T21:11:10.000Z
# Language: Python3
# Runtime: 9 ms · Beats 27.26%
# Memory: 20.7 MB · Beats 62.32%
# Submission: https://leetcode.com/submissions/detail/2138973185/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #original = [row[:] for row in matrix]

        i_zeros = set()
        j_zeros = set()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m) : 
            for j in range(n) : 
                if matrix[i][j] == 0 :
                    i_zeros.add(i)
                    j_zeros.add(j)
        
        for i in range(m) : 
            for j in range(n) : 
                if i in i_zeros or j in j_zeros: 
                    matrix[i][j] = 0
