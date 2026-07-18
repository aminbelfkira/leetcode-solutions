# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# Accepted: 2026-07-18T18:14:03.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 7 ms · Beats 81.2%
# Memory: 23.9 MB · Beats 5.25%
# Submission: https://leetcode.com/submissions/detail/2072679845/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char.lower() for char in s if char.isalnum()]
        return s == s[::-1]
