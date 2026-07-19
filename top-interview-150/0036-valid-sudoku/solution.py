# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/
# Accepted: 2026-07-19T12:12:08.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 2 ms · Beats 79.41%
# Memory: 19.3 MB · Beats 34.43%
# Submission: https://leetcode.com/submissions/detail/2073434713/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        square = [set() for _ in range(9)]

        for i in range(9) : 
            for j in range(9) : 

                num = board[i][j]

                if num == "." : 
                    continue

                num_square = 3*(i//3) + j//3

                if num in rows[i] or num in cols[j] or num in square[num_square] : 
                    return False
                
                rows[i].add(num)
                cols[j].add(num)
                square[num_square].add(num)
        
        return True
