# 73. Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/
# Accepted: 2026-09-04T13:34:38.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 7 ms · Beats 57.11%
# Memory: 20.7 MB · Beats 55.55%
# Submission: https://leetcode.com/submissions/detail/2130740980/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
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
                if i in i_zeros or j in j_zeros : 
                    matrix[i][j] = 0 
