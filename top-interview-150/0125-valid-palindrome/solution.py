# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# Accepted: 2026-07-18T17:06:14.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 9 ms · Beats 41.88%
# Memory: 23.4 MB · Beats 7.8%
# Submission: https://leetcode.com/submissions/detail/2072597663/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char.lower() for char in s if char.isalnum()]
        n = len(s)
        left, right = 0, n-1

        while left < right : 

            if s[left]== s[right] : 
                left +=1
                right -=1
            else : 
                return False

        return True 
