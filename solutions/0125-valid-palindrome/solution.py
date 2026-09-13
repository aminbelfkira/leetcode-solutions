# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# Accepted: 2026-09-13T21:27:04.000Z
# Language: Python3
# Runtime: 8 ms · Beats 48.63%
# Memory: 24.1 MB · Beats 5.98%
# Submission: https://leetcode.com/submissions/detail/2141026589/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = [char.lower() for char in s if char.isalnum()]
        return s == s[::-1]
