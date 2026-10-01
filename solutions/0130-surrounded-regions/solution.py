# 130. Surrounded Regions
# https://leetcode.com/problems/surrounded-regions/
# Accepted: 2026-10-01T12:55:15.000Z
# Language: Python3
# Runtime: 3 ms · Beats 84.58%
# Memory: 22.3 MB · Beats 60.89%
# Submission: https://leetcode.com/submissions/detail/2159202945/

class Solution:
    def solve(self, grid: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(grid)
        n = len(grid[0]) 

        def aux(r,c) : 
            if not (0<= r< m and 0 <= c< n) : 
                return
            if grid[r][c] == "O" : 
                grid[r][c] = "#"
                aux(r+1, c)
                aux(r-1, c)
                aux(r, c+1)
                aux(r, c-1)
        for i in range(m) :
            aux(i, 0)
            aux(i, n-1)
        for j in range(n) : 
            aux(0, j)
            aux(m-1, j)

        for i in range(m) : 
            for j in range(n) : 
                if grid[i][j] == "O" : 
                    grid[i][j] = "X"
                elif grid[i][j] == "#" : 
                    grid[i][j] = "O"
                else :
                    continue 
