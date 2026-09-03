# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/
# Accepted: 2026-09-03T20:35:46.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 16.45%
# Submission: https://leetcode.com/submissions/detail/2130083876/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        return len(s.split()[-1])
        
