# 289. Game of Life
# https://leetcode.com/problems/game-of-life/
# Accepted: 2026-07-20T22:33:55.000Z
# Language: Python3
# Runtime: 4 ms · Beats 5.73%
# Memory: 19.3 MB · Beats 47.33%
# Submission: https://leetcode.com/submissions/detail/2075118762/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        original = [row[:] for row in board]

        def count_neighbors(board, i,j) : 
            count = 0
            for di in (-1,0,1) :
                for dj in (-1,0,1) : 
                    if di ==0 and dj ==0 : 
                        continue
                    
                    ni = i+di
                    nj = j+dj
                    if 0<=ni<m and 0<=nj<n : 
                        if board[ni][nj] : 
                            count+=1 
            return count
        
        for i in range(m) :
            for j in range(n) : 

                alive = count_neighbors(original, i,j)
                num_board = original[i][j]
                if num_board and alive <2 : 
                    board[i][j] = 0
                elif num_board and alive in (2,3) : 
                    continue
                elif num_board and alive>3 : 
                    board[i][j] = 0
                elif num_board ==0 and alive ==3 : 
                    board[i][j] = 1
        
