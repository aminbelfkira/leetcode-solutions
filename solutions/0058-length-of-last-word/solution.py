# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/
# Accepted: 2026-10-07T06:31:51.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.2 MB · Beats 87.88%
# Submission: https://leetcode.com/submissions/detail/2164996842/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        return len(s.split()[-1])
