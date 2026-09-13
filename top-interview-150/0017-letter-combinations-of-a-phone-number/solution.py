# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Accepted: 2026-09-13T16:29:20.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.2 MB · Beats 95.84%
# Submission: https://leetcode.com/submissions/detail/2140795578/

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
        combinations = ['']
        for digit in digits : 
            combinations = [prefix + char for prefix in combinations for char in letters[digit]]
        return combinations 
