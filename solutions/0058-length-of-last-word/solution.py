# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/
# Accepted: 2026-09-11T22:20:59.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 53.82%
# Submission: https://leetcode.com/submissions/detail/2138996253/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
