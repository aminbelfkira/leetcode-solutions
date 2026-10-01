# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/
# Accepted: 2026-10-01T08:25:12.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.6 MB · Beats 42.52%
# Submission: https://leetcode.com/submissions/detail/2159000689/

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m
        while left < right : 
            mid = (left + right)//2
            if matrix[mid][0] <= target : 
                left= mid +1
            else : 
                right = mid

        row = left -1 
        left = 0
        right = n-1
        while left <= right : 
            mid = (left + right)//2
            if matrix[row][mid] == target : 
                return True
            elif matrix[row][mid] > target : 
                right = mid -1
            else : 
                left = mid +1
        return False
