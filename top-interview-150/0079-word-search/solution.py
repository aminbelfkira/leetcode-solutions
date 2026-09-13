# 79. Word Search
# https://leetcode.com/problems/word-search/
# Accepted: 2026-09-13T17:43:30.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 3252 ms · Beats 84.03%
# Memory: 19.6 MB · Beats 28.83%
# Submission: https://leetcode.com/submissions/detail/2140871260/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        if len(word) > rows * cols : 
            return False
        
        def backtrack(row, col, index) : 
            if (not(0 <= row < rows and 0 <= col < cols) or board[row][col] != word[index]) : 
                return False
            if index == len(word) - 1 : 
                return True
            char = board[row][col] 
            board[row][col] = "#"
            found = backtrack(row +1, col ,index +1) or backtrack(row -1, col , index +1) or backtrack(row, col +1, index +1) or backtrack(row, col -1, index +1)
            board[row][col] = char
            return found
        return any(backtrack(row, col, 0) for row in range(rows) for col in range(cols))
