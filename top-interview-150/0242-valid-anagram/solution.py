# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/
# Accepted: 2026-07-20T23:20:25.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 3 ms · Beats 98.45%
# Memory: 19.6 MB · Beats 25.99%
# Submission: https://leetcode.com/submissions/detail/2075131570/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        from collections import Counter

        return Counter(s) == Counter(t)
