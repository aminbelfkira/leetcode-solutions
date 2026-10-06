# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/
# Accepted: 2026-10-06T14:34:42.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 80.55%
# Submission: https://leetcode.com/submissions/detail/2164333626/

class Solution:
    def reverseWords(self, s: str) -> str:

        return " ".join(s.split()[::-1])
        
