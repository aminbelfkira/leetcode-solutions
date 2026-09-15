# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/
# Accepted: 2026-09-15T15:16:06.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.6 MB · Beats 14.08%
# Submission: https://leetcode.com/submissions/detail/2142733936/

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        left = 0
        right = len(matrix)
        while left < right : 
            mid = (left + right)//2
            if matrix[mid][0]<=target : 
                left = mid +1
            else : 
                right = mid
        
        row_target = left -1
        print(row_target)
        left = 0
        right = len(matrix[0]) -1
        while left <= right :
            mid = (left + right)//2
            if matrix[row_target][mid] == target : 
                return True
            if matrix[row_target][mid]< target :
                left = mid +1
            else : 
                right = mid -1
        return False

