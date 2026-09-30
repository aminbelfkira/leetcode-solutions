# 79. Word Search
# https://leetcode.com/problems/word-search/
# Accepted: 2026-09-30T23:05:22.000Z
# Language: Python3
# Runtime: 3602 ms · Beats 59.62%
# Memory: 19.6 MB · Beats 29.31%
# Submission: https://leetcode.com/submissions/detail/2158636791/

class Solution:
    def exist(self, grid: list[list[str]], word: str) -> bool:
        m= len(grid)
        n = len(grid[0])

        def aux(r,c, i) : 
            if i == len(word) :
                return True
            if not(0<=r<m and 0<=c<n) : 
                return False
            if grid[r][c] == word[i] :
                temp = grid[r][c]
                grid[r][c] = "#"
                res = aux(r+1,c, i+1) or aux(r-1,c, i+1) or aux(r, c+1, i+1) or aux(r, c-1, i+1)
                grid[r][c] = temp
                return res
            else  : 
                return False
        for i in range(m) : 
            for j in range(n) : 
                res = aux(i,j,0) 
                if res :
                    return True
        return False
