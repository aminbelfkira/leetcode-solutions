# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/
# Accepted: 2026-09-04T13:02:03.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.5 MB · Beats 7.76%
# Submission: https://leetcode.com/submissions/detail/2130711427/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m = len(matrix)
        n = len(matrix[0])

        k = 0 
        left = 0
        top = 0
        bottom = m-1
        right = n-1
        
        res = []

        while k < m*n : 

            for j in range(left, right +1) : 
                res.append(matrix[top][j])
                k+=1
            top += 1
            #print(top)
            for i in range(top, bottom +1) : 
                res.append(matrix[i][right]) 
                k+=1
            right -=1

            if top <= bottom : 
                for i in range(right, left -1, -1) : 
                    res.append(matrix[bottom][i])
                    k+=1
                bottom -=1
            if left <= right : 
                for i in range(bottom, top-1 ,-1 ) : 
                    res.append(matrix[i][left])
                    k+=1
                left +=1
        return res

                

