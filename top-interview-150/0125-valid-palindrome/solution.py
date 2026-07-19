# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# Accepted: 2026-07-19T01:33:58.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 3 ms · Beats 99%
# Memory: 23.8 MB · Beats 5.25%
# Submission: https://leetcode.com/submissions/detail/2072873867/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char.lower() for char in s if char.isalnum()]
        return s == s[::-1]
