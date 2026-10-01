# 201. Bitwise AND of Numbers Range
# https://leetcode.com/problems/bitwise-and-of-numbers-range/
# Accepted: 2026-10-01T14:50:45.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 3 ms · Beats 73.11%
# Memory: 19.3 MB · Beats 54.77%
# Submission: https://leetcode.com/submissions/detail/2159302345/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shifts = 0
        while left != right : 
            left >>=1
            right >>=1
            shifts +=1
        return left << shifts 
