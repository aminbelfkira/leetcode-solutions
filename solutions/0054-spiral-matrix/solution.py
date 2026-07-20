# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/
# Accepted: 2026-07-20T22:16:01.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 72.68%
# Submission: https://leetcode.com/submissions/detail/2075113463/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m = len(matrix)
        n = len(matrix[0])
        results = []
        k = 0

        top, bottom = 0, m -1
        left, right = 0, n -1

        while k < n*m : 

            for i in range(left, right+1) : 
                results.append(matrix[top][i])
                k+=1
            top +=1

            for i in range(top, bottom+1) : 
                results.append(matrix[i][right])
                k+=1
            right -=1

            if top<=bottom : 

                for i in range(right, left -1, -1) : 
                    results.append(matrix[bottom][i])
                    k+=1
                bottom-=1
            
            if left<=right : 

                for i in range(bottom, top-1, -1) :
                    results.append(matrix[i][left])
                    k+=1
                left +=1

        return results 
