# 6. Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/
# Accepted: 2026-07-21T23:09:55.000Z
# Language: Python3
# Runtime: 7 ms · Beats 84.66%
# Memory: 19.4 MB · Beats 46.54%
# Submission: https://leetcode.com/submissions/detail/2076419300/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows ==1 : 
            return s

        direction = -1
        rows = [''] * numRows
        current_row = 0
        for char in s : 
            rows[current_row] += char
            if current_row == 0 or current_row == numRows - 1:
                direction = -direction  
            current_row += direction
        return ''.join(rows)
