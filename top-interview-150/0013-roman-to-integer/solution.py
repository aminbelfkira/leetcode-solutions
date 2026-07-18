# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/
# Accepted: 2026-07-18T23:21:42.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 11 ms · Beats 14.24%
# Memory: 19.2 MB · Beats 57.37%
# Submission: https://leetcode.com/submissions/detail/2072840532/

class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_to_integer = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50 , 'C' : 100, 'D' :500, 'M' : 1000}
        n = len(s)
        result =0
        for i in range(n) : 

            if i+1 < n and roman_to_integer[s[i]] < roman_to_integer[s[i+1]] : 
                result -= roman_to_integer[s[i]]
            else : 
                result += roman_to_integer[s[i]]
        
        return result
