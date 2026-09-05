# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/
# Accepted: 2026-09-05T15:20:17.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 7 ms · Beats 91.71%
# Memory: 19.4 MB · Beats 76.25%
# Submission: https://leetcode.com/submissions/detail/2131856809/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        return Counter(s) == Counter(t)
