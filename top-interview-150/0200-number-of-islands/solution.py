# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/
# Accepted: 2026-09-12T21:06:15.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 241 ms · Beats 63.11%
# Memory: 21.4 MB · Beats 92.04%
# Submission: https://leetcode.com/submissions/detail/2140008300/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0] : 
            return 0
        
        rows, cols = len(grid), len(grid[0])
        directions = ((1,0), (-1, 0), (0,1), (0, -1))
        islands = 0
        for row in range(rows) :
            for col in range(cols) : 
                if grid[row][col] != "1" : 
                    continue
                
                islands +=1
                grid[row][col] = "0"
                stack = [(row, col)]
                while stack : 
                    r, c = stack.pop()
                    for dr, dc in  directions :
                        nr, nc = r+dr, c+dc

                        if (0 <= nr < rows and 0<= nc < cols and grid[nr][nc] == "1") : 
                            grid[nr][nc] = "0"
                            stack.append((nr, nc))
        return islands
