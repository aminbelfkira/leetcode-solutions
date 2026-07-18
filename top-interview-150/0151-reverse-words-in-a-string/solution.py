# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/
# Accepted: 2026-07-18T23:46:18.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 39.93%
# Submission: https://leetcode.com/submissions/detail/2072846781/

class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.split()[::-1]

        return " ".join(s)
