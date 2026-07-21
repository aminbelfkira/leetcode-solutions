# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/
# Accepted: 2026-07-21T23:26:06.000Z
# Language: Python3
# Runtime: 5 ms · Beats 36.53%
# Memory: 19.4 MB · Beats 9.53%
# Submission: https://leetcode.com/submissions/detail/2076423744/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for i in range(9) : 
            for j in range(9) : 

                num = board[i][j]  
                if num == "." : 
                    continue
                
                num_square = 3*(i//3) + j//3
                if num in rows[i] or num in cols[j] or num in squares[num_square] : 
                    return False
                rows[i].add(num)
                cols[j].add(num)
                squares[num_square].add(num)
        
        return True
