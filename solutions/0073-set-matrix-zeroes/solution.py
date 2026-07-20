# 73. Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/
# Accepted: 2026-07-20T22:23:08.000Z
# Language: Python3
# Runtime: 7 ms · Beats 58.68%
# Memory: 20.8 MB · Beats 15.02%
# Submission: https://leetcode.com/submissions/detail/2075115675/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n =len(matrix[0])
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
