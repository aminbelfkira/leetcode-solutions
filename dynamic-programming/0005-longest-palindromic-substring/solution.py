# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
# Accepted: 2026-08-11T02:32:51.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 211 ms · Beats 92.49%
# Memory: 19.2 MB · Beats 68.68%
# Submission: https://leetcode.com/submissions/detail/2102185877/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def expand(left, right) :
            while left >=0 and right<n and s[left] == s[right] : 
                left -=1
                right +=1
            
            return s[left+1: right ]
        maxpalindrome = ""
        for i in range(n) : 
            even = expand(i,i+1)
            odd = expand(i, i)
            maxpalindrome = max(even, odd, maxpalindrome, key = len)
        return maxpalindrome
