# 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Accepted: 2026-07-19T00:17:29.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 3 ms · Beats 19.06%
# Memory: 19.4 MB · Beats 8.03%
# Submission: https://leetcode.com/submissions/detail/2072854521/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle) 

        for i in range(len(haystack)) : 
            if haystack[i:i+n]== needle : 
                return i
        return -1
