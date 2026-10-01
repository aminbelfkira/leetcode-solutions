# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/
# Accepted: 2026-10-01T14:55:28.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 8 ms · Beats 54.02%
# Memory: 19.1 MB · Beats 87.21%
# Submission: https://leetcode.com/submissions/detail/2159306559/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        return x_str == x_str[::-1]
