# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# Accepted: 2026-10-07T06:34:53.000Z
# Language: Python3
# Runtime: 11 ms · Beats 31.88%
# Memory: 23.4 MB · Beats 8.26%
# Submission: https://leetcode.com/submissions/detail/2164999586/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char.lower() for char in s if char.isalnum()]
        left = 0 
        right = len(s)-1
        while left < right : 
            if s[left] != s[right] : 
                return False
            left +=1
            right-=1
        return True
