# 6. Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/
# Accepted: 2026-09-11T16:35:12.000Z
# Language: Python3
# Runtime: 2 ms · Beats 99%
# Memory: 19.3 MB · Beats 46.3%
# Submission: https://leetcode.com/submissions/detail/2138751093/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 :
            return s 
        current = 0
        direction = -1
        rows = [''] * numRows
        for char in s : 
            rows[current]+= char
            if current == 0 or current == numRows -1 : 
                direction = -direction
            current += direction
        return ''.join(rows)
