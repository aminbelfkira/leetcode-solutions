# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/
# Accepted: 2026-09-18T14:34:05.000Z
# Language: Python3
# Runtime: 228 ms · Beats 90.24%
# Memory: 21.6 MB · Beats 48.87%
# Submission: https://leetcode.com/submissions/detail/2145824292/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0
        def dfs(r,c) : 
            nonlocal islands
            if not(0<= r< m and 0 <= c < n) :
                return
            if grid[r][c] == "1":
                grid[r][c] = "0"
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)
        for i in range(m) : 
            for j in range(n) :
                if grid[i][j] == "1": 
                    islands +=1
                    dfs(i,j)
        return islands
