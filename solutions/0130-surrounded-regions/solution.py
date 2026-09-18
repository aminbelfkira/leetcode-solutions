# 130. Surrounded Regions
# https://leetcode.com/problems/surrounded-regions/
# Accepted: 2026-09-18T14:37:25.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 22.4 MB · Beats 60.39%
# Submission: https://leetcode.com/submissions/detail/2145827037/

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        islands = 0
        def dfs(r,c) : 
            if not(0 <= r < m and 0 <= c < n) : 
                return
            if board[r][c] == "O" : 
                board[r][c] = "#"
                dfs(r+1,c)
                dfs(r-1, c) 
                dfs(r, c+1)
                dfs(r, c-1)
        
        for i in range(m) : 
            dfs(i, 0)
            dfs(i, n-1)
        for j in range(n) : 
            dfs(0, j)
            dfs(m-1, j)
        
        for r in range(m) : 
            for c in range(n) : 
                if board[r][c] == "O" : 
                    board[r][c] = "X"
                if board[r][c] == "#" : 
                    board[r][c] = "O"
