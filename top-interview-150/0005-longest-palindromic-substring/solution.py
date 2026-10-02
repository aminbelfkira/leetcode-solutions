# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
# Accepted: 2026-10-02T18:59:30.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 219 ms · Beats 89.97%
# Memory: 19.5 MB · Beats 19.23%
# Submission: https://leetcode.com/submissions/detail/2160493189/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        def aux(left, right) :
            while left >= 0 and right<n and s[left] == s[right] :
                left -=1
                right +=1
            return s[left+1 : right]
        
        maxpalindrome = ""
        for i in range(n) : 
            even = aux(i, i+1)
            odd = aux(i,i)
            maxpalindrome = max(even, odd, maxpalindrome, key = len)
        return maxpalindrome
