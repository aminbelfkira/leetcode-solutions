# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/
# Accepted: 2026-09-14T14:14:20.000Z
# Language: Python3
# Runtime: 236 ms · Beats 76.47%
# Memory: 21.7 MB · Beats 48.55%
# Submission: https://leetcode.com/submissions/detail/2141637341/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0] :
            return 0
        stack = []
        m = len(grid)
        n = len(grid[0])
        def dfs(r,c) : 
            if not( 0 <= r< m and 0<= c < n ):
                return
            if grid[r][c] == "1" : 
                grid[r][c] = "0"
                dfs(r+1, c)
                dfs(r-1,c)
                dfs(r, c-1)
                dfs(r, c+1)
            else : 
                return
        islands = 0
        for i in range(m) : 
            for j in range(n) : 
                if grid[i][j] == "1" :
                    dfs(i,j) 
                    islands +=1
        return islands

