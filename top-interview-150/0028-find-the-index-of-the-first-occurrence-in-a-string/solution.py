# 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Accepted: 2026-09-03T20:53:29.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 3 ms · Beats 18.24%
# Memory: 19.3 MB · Beats 27.22%
# Submission: https://leetcode.com/submissions/detail/2130092751/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle) 

        for i in range(len(haystack)) : 
            if haystack[i:i+n]== needle : 
                return i
        return -1
