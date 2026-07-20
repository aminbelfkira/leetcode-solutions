# 73. Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/
# Accepted: 2026-07-20T22:21:51.000Z
# Language: Python3
# Runtime: 11 ms · Beats 25.97%
# Memory: 20.7 MB · Beats 15.02%
# Submission: https://leetcode.com/submissions/detail/2075115267/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m, n = len(matrix), len(matrix[0])
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
                    matrix[i][j] =0
