# 289. Game of Life
# https://leetcode.com/problems/game-of-life/
# Accepted: 2026-07-19T14:22:23.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 47.21%
# Submission: https://leetcode.com/submissions/detail/2073554716/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        original = [row[:] for row in board]

        def count_neighbors(i,j) : 
            count = 0
            for di in (-1,0,1) : 
                for dj in (-1,0,1) : 
                    if di == 0 and dj ==0 : 
                        continue
                    new_i = i+di
                    new_j = j+dj
                    if 0<= new_i < m and 0<= new_j < n : 
                        count += original[new_i][new_j]
            return count
        
        for i in range(m) : 
            for j in range(n) : 
                alive = count_neighbors(i,j)
                if original[i][j] == 1 and alive not in (2,3) : 
                    board[i][j] = 0
                elif original[i][j] == 0 and alive ==3 : 
                    board[i][j] = 1
