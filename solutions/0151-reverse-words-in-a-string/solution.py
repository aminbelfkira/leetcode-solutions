# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/
# Accepted: 2026-09-14T13:32:52.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 11.47%
# Submission: https://leetcode.com/submissions/detail/2141598857/

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
