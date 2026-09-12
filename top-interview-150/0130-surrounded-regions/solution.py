# 130. Surrounded Regions
# https://leetcode.com/problems/surrounded-regions/
# Accepted: 2026-09-12T21:39:10.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 5 ms · Beats 61.18%
# Memory: 22.4 MB · Beats 60.21%
# Submission: https://leetcode.com/submissions/detail/2140021309/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0] : 
            return
        
        rows, cols = len(board), len(board[0])
        stack = []

        def mark(r, c) : 
            if board[r][c] == "O" : 
                board[r][c] = "#"
                stack.append((r,c))
        
        for r in range(rows) : 
            mark(r,0)
            mark(r, cols-1)
        for c in range(cols) : 
            mark(0, c)
            mark(rows-1, c)
        
        directions =((1, 0), (-1, 0), (0, 1), (0, -1))
        while stack : 
            r,c = stack.pop()
            for dr, dc in directions : 
                nr, nc = r +dr, c+dc

                if 0<= nr < rows and 0 <= nc < cols :
                    nr, nc = r+dr, c+dc
                    if 0<= nr < rows and 0 <= nc < cols :
                        mark(nr, nc)
        
        for r in range(rows) : 
            for c in range(cols) : 
                if board[r][c] == "O" : 
                    board[r][c] = "X"
                elif board[r][c] == "#" : 
                    board[r][c] = "O"
