# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/
# Accepted: 2026-09-13T19:29:15.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.1 MB · Beats 99.3%
# Submission: https://leetcode.com/submissions/detail/2140966055/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = n-1
        bottom = m-1
        top = 0
        k = 0
        res = []
        while k < m*n : 
            for j in range(left, right +1) : 
                res.append(matrix[top][j])
                k+=1
            top +=1
            for i in range(top, bottom +1) : 
                res.append(matrix[i][right])
                k+=1
            right -=1

            if top <= bottom : 
                for j in range(right, left -1, -1) :
                    res.append(matrix[bottom][j])
                    k+=1
                bottom-=1
            if left <= right : 
                for i in range(bottom, top -1, -1) : 
                    res.append(matrix[i][left])
                    k+=1
                left +=1
        return res
