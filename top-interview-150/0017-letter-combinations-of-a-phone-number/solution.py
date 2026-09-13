# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Accepted: 2026-09-13T16:31:16.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 78.36%
# Submission: https://leetcode.com/submissions/detail/2140797353/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits : 
            return []
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []
        path = []
        def backtrack(index) : 
            if index == len(digits) : 
                result.append(''.join(path))
                return
            for char in letters[digits[index]] : 
                path.append(char)
                backtrack(index +1)
                path.pop()
        backtrack(0)
        return result
