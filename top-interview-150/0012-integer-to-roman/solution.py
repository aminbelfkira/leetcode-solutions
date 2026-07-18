# 12. Integer to Roman
# https://leetcode.com/problems/integer-to-roman/
# Accepted: 2026-07-18T23:31:03.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 25.41%
# Submission: https://leetcode.com/submissions/detail/2072842844/

class Solution:
    def intToRoman(self, num: int) -> str:
        
        values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        reste = num
        result = ""
        for i in range(len(values)) : 
            q, d = divmod(reste, values[i])
            result += q * symbols[i]
            reste = d
        
        return result


