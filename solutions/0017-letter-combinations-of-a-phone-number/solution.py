# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Accepted: 2026-10-06T12:16:06.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.5 MB · Beats 10.58%
# Submission: https://leetcode.com/submissions/detail/2164203190/

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        letters = {
            "0" : "",
            "1" : "",
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs", 
            "8" : "tuv",
            "9" : "wxyz"
        }
        res = []
        current = []
        n = len(digits)
        def aux(i) :
            if i > n : 
                return
            if len(current) == n : 
                res.append("".join(current))
                return

            for letter in (letters[digits[i]]) : 
                current.append(letter)
                aux(i+1)
                current.pop()
        
        aux(0)
        return res
