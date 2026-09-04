# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/
# Accepted: 2026-09-04T12:45:22.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 1 ms · Beats 83%
# Memory: 19.4 MB · Beats 35.64%
# Submission: https://leetcode.com/submissions/detail/2130697005/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        square_set = [set() for _ in range(9)]

        for i in range(9) : 
            for j in range(9) : 

                num_board = board[i][j]
                if num_board == "." : 
                    continue
                num_square = (i//3) * 3 + j//3
                if num_board in row_set[i] or num_board in col_set[j] or num_board in square_set[num_square] : 
                    return False
                
                row_set[i].add(num_board)
                col_set[j].add(num_board)
                square_set[num_square].add(num_board)
        return True
