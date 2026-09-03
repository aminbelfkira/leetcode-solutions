# 6. Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/
# Accepted: 2026-09-03T20:50:14.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 7 ms · Beats 83.48%
# Memory: 19.5 MB · Beats 19.27%
# Submission: https://leetcode.com/submissions/detail/2130091177/

class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1 : 
            return s
        direction = -1
        rows = [''] *num_rows
        current_row = 0

        for char in s : 
            rows[current_row] += char
            if current_row == 0 or current_row == num_rows -1 : 
                direction = - direction
            current_row += direction
        return "".join(rows)

