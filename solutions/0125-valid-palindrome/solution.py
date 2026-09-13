# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# Accepted: 2026-09-13T21:28:04.000Z
# Language: Python3
# Runtime: 7 ms · Beats 80.71%
# Memory: 23.6 MB · Beats 5.98%
# Submission: https://leetcode.com/submissions/detail/2141026974/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = [char.lower() for char in s if char.isalnum()]
        left = 0
        right = len(s)-1
        while left< right : 
            if s[left] != s[right] : 
                return False
            left +=1
            right -=1
        return True
