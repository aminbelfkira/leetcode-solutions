# 79. Word Search
# https://leetcode.com/problems/word-search/
# Accepted: 2026-09-21T11:30:50.000Z
# Language: Python3
# Runtime: 3239 ms · Beats 84.28%
# Memory: 19.4 MB · Beats 59.89%
# Submission: https://leetcode.com/submissions/detail/2148581183/

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        if len(word) > rows * cols : 
            return False
        def backtrack(r,c,index) : 

            if not (0<=r<rows and 0<= c < cols) or board[r][c] != word[index] : 
                return False
            if index == len(word) - 1 : 
                return True

            char = board[r][c]
            board[r][c] = "#"
            found = backtrack(r+1, c, index +1) or backtrack(r-1, c, index +1) or backtrack(r, c-1, index+1) or backtrack(r,c+1, index +1)
            board[r][c] = char
            return found

        return any(backtrack(r,c,0) for r in range(rows) for c in range(cols)) 
