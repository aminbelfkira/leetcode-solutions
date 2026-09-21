# 434. Number of Segments in a String
# https://leetcode.com/problems/number-of-segments-in-a-string/
# Accepted: 2026-09-21T10:53:51.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.2 MB · Beats 48.12%
# Submission: https://leetcode.com/submissions/detail/2148554829/

class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
