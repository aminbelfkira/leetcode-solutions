# 73. Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/
# Accepted: 2026-07-19T14:12:17.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 20.6 MB · Beats 15.92%
# Submission: https://leetcode.com/submissions/detail/2073544648/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])

        i_zeros = set()
        j_zeros = set()

        for i in range(m) : 
            for j in range(n) : 

                if matrix[i][j] == 0 : 
                    i_zeros.add(i)
                    j_zeros.add(j)

        for i in range(m) : 
            for j in range(n) : 
                if i in i_zeros or j in j_zeros : 
                    matrix[i][j] = 0
        
