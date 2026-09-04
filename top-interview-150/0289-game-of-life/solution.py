# 289. Game of Life
# https://leetcode.com/problems/game-of-life/
# Accepted: 2026-09-04T13:44:30.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.5 MB · Beats 15.98%
# Submission: https://leetcode.com/submissions/detail/2130750308/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        original = [row[:] for row in board]

        for i in range(m) : 
            for j in range(n) : 
                neighbors  =0 
                
                for di in (-1,0,1) :
                    for dj in (-1,0,1) :
                        ni = i+di
                        nj = j+dj
                        if 0<=ni<m and 0<=nj <n and not (i==ni and j==nj) : 
                            neighbors += original[ni][nj]
                if original[i][j] and neighbors < 2 : 
                    board[i][j] =0
                elif original[i][j] and neighbors in (2,3) : 
                    board[i][j] = 1
                elif original[i][j] and neighbors > 3 : 
                    board[i][j] = 0
                elif not original[i][j] and neighbors == 3 : 
                    board[i][j] = 1
                else : 
                    board[i][j] = 0
