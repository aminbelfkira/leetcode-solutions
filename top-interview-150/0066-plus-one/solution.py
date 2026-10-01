# 66. Plus One
# https://leetcode.com/problems/plus-one/
# Accepted: 2026-10-01T14:57:54.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 3 ms · Beats 3.04%
# Memory: 19.2 MB · Beats 88.65%
# Submission: https://leetcode.com/submissions/detail/2159308726/

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1) : 
            total = digits[i] + carry
            digits[i] = total%10
            carry = total //10
        
        if carry : 
            return [1] + digits
        return digits
