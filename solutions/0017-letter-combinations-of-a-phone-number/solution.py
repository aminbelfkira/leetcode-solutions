# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Accepted: 2026-09-21T10:58:02.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 10.32%
# Submission: https://leetcode.com/submissions/detail/2148558033/

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        
        letters = {
            "0" : "",
            "1":"",
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
        def aux(start) :
            if len(current) == len(digits) :
                res.append("".join(current))
                return
            for letter in letters[digits[start]] : 
                current.append(letter)
                aux(start+1)
                current.pop()
        aux(0)
        return res
            
