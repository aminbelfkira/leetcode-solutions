# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Accepted: 2026-09-14T20:44:34.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 41.33%
# Submission: https://leetcode.com/submissions/detail/2141994739/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dico = {
            "0" : "",
            "1" : "",
            "2" : "abc",
            "3": "def", 
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        path = []
        result = []

        def backtrack() : 
            if len(path) == len(digits) : 
                res = path.copy()

                result.append("".join(res))
                return
            n = len(path)
            for letter in dico[digits[n]] : 
                path.append(letter)
                backtrack()
                path.pop()
        backtrack()
        return result
