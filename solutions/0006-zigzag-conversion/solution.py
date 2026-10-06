# 6. Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/
# Accepted: 2026-10-06T13:46:04.000Z
# Language: Python3
# Runtime: 4 ms · Beats 94.24%
# Memory: 19.2 MB · Beats 96.6%
# Submission: https://leetcode.com/submissions/detail/2164282857/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 : 
            return s
        rows = [''] *numRows
        direction = -1
        current_row = 0
        for char in s : 
            rows[current_row] +=char
            if current_row == 0  : 
                direction = 1
            if current_row == numRows -1 : 
                direction = -1
            current_row += direction
        return "".join(rows)
            
