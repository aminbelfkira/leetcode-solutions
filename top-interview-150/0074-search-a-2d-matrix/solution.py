# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/
# Accepted: 2026-09-13T18:58:39.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.5 MB · Beats 79.69%
# Submission: https://leetcode.com/submissions/detail/2140944039/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m
        while left < right :
            mid = (left + right) //2
            if matrix[mid][0] <= target : 
                left = mid +1
            else : 
                right = mid
        if left == 0 :
            return False 
        
        row= matrix[left -1]
        left, right = 0, len(row) -1
        while left <= right : 
            mid = (left + right)//2
            if row[mid] == target : 
                return True
            elif row[mid] < target : 
                left = mid +1
            else :
                right = mid -1
        
        return False

