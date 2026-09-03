# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/
# Accepted: 2026-09-03T20:42:34.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 40.74%
# Submission: https://leetcode.com/submissions/detail/2130087494/

class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split()
        return " ".join(words[::-1])
