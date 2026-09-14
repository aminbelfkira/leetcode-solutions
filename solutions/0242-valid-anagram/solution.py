# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/
# Accepted: 2026-09-14T13:14:39.000Z
# Language: Python3
# Runtime: 7 ms · Beats 91.84%
# Memory: 19.3 MB · Beats 76.06%
# Submission: https://leetcode.com/submissions/detail/2141582139/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter 
        return Counter(s) == Counter(t)
