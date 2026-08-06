# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Accepted: 2026-08-06T10:57:10.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 40.24%
# Submission: https://leetcode.com/submissions/detail/2096561207/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }

        result = []
        current = ""

        def backtrack(digit_str):
            nonlocal current
            if not digit_str:
                result.append(current)
                return

            for letter in phone[digit_str[0]]:
                tmp = current
                current += letter
                backtrack(digit_str[1:])
                current = tmp

        backtrack(digits)
        return result
