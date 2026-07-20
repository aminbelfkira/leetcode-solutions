# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/
# Accepted: 2026-07-20T22:53:48.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 4 ms · Beats 59.61%
# Memory: 19.2 MB · Beats 82.09%
# Submission: https://leetcode.com/submissions/detail/2075124478/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))
