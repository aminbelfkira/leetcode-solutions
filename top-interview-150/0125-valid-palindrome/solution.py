# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# Accepted: 2026-09-03T20:57:19.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 8 ms · Beats 48.96%
# Memory: 24.2 MB · Beats 5.74%
# Submission: https://leetcode.com/submissions/detail/2130094665/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char.lower() for char in s if char.isalnum() ]
        print(s)
        return s == s[::-1]
