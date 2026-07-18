# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/
# Accepted: 2026-07-18T23:31:54.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 52.19%
# Submission: https://leetcode.com/submissions/detail/2072843059/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        return len(s.split()[-1])
