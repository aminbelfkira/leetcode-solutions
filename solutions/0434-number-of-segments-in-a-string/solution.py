# 434. Number of Segments in a String
# https://leetcode.com/problems/number-of-segments-in-a-string/
# Accepted: 2026-10-06T12:58:57.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 49%
# Submission: https://leetcode.com/submissions/detail/2164237445/

class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
