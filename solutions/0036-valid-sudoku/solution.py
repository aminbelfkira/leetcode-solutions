# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/
# Accepted: 2026-09-13T21:44:06.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 74.62%
# Submission: https://leetcode.com/submissions/detail/2141032900/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        square_set = [set() for _ in range(9)]
        
        for i in range(9) : 
            for j in range(9) :
                num = board[i][j]

                if num == "." :
                    continue
                num_square = (i//3) * 3 + j //3
                if num in row_set[i] or num in col_set[j] or num in square_set[num_square] : 
                    return False
                row_set[i].add(num)
                col_set[j].add(num)
                square_set[num_square].add(num)

        return True
