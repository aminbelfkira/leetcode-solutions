# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/
# Accepted: 2026-09-11T16:53:04.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 73.68%
# Submission: https://leetcode.com/submissions/detail/2138770495/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        bottom = m-1
        left = 0 
        right = n-1
        k = 0
        res = []
        while k <m*n : 

            for j in range(left, right +1) : 
                res.append(matrix[top][j])
                k+=1
            top +=1

            for i in range(top, bottom +1) :
                res.append(matrix[i][right])
                k+=1
            right -=1

            if top <= bottom : 
                for i in range(right, left -1, -1) : 
                    res.append(matrix[bottom][i])
                    k+=1
                bottom -=1
            
            if left <=right :
                for j in range(bottom,top -1, -1): 
                    res.append(matrix[j][left])
                    k+=1
                left +=1
        
        return res
