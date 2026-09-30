# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/
# Accepted: 2026-09-30T21:47:33.000Z
# Language: Python3
# Runtime: 231 ms · Beats 86.13%
# Memory: 21.5 MB · Beats 73.77%
# Submission: https://leetcode.com/submissions/detail/2158615069/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        def aux(r,c) : 
            if not (0<= r < m and 0<= c< n) : 
                return
            if grid[r][c] == "1" : 
                grid[r][c] = "0"
                aux(r+1, c)
                aux(r-1, c)
                aux(r, c+1)
                aux(r, c-1)
        islands = 0
        for i in range(m) :
            for j in range(n) : 
                if grid[i][j] == "1" : 
                    islands +=1
                    aux(i,j)
        return islands
