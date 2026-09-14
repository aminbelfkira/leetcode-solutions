# 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Accepted: 2026-09-14T13:40:26.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.5 MB · Beats 8.9%
# Submission: https://leetcode.com/submissions/detail/2141605606/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
