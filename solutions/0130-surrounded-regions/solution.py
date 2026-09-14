# 130. Surrounded Regions
# https://leetcode.com/problems/surrounded-regions/
# Accepted: 2026-09-14T14:27:19.000Z
# Language: Python3
# Runtime: 3 ms · Beats 84.42%
# Memory: 22.3 MB · Beats 78.11%
# Submission: https://leetcode.com/submissions/detail/2141650005/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board) 
        n = len(board[0])

        def dfs(r,c) :
            if not (0<=r<m and 0 <=c<n) : 
                return 
            if board[r][c] == "O":
                board[r][c] = "#"
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)
        for i in range(m) :
            if board[i][0] == "O" : 
                dfs(i,0)
            if board[i][n-1] == "O" : 
                dfs(i, n-1)
        for j in range(n) : 
            if board[0][j] == "O" :
                dfs(0,j)
            if board[m-1][j] == "O" : 
                dfs(m-1,j)
        for i in range(m) : 
            for j in range(n) : 
                if board[i][j] == '#' : 
                    board[i][j] = "O"
                elif board[i][j] =="O":
                    board[i][j] = "X"
                else : 
                    continue
        
