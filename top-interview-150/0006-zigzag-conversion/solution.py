# 6. Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/
# Accepted: 2026-07-19T00:14:12.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 11 ms · Beats 54.06%
# Memory: 19.5 MB · Beats 21.38%
# Submission: https://leetcode.com/submissions/detail/2072853683/

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
