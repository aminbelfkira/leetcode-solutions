# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/
# Accepted: 2026-09-05T11:36:54.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 4 ms · Beats 61.73%
# Memory: 19.2 MB · Beats 83.16%
# Submission: https://leetcode.com/submissions/detail/2131656847/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        if len(s) != len(t) : 
            return False
        n = len(s)
        for i, (char_s, char_t) in enumerate(zip(s, t)) : 

            if char_s in s_to_t and char_t != s_to_t[char_s] :
                return False
            if char_t in t_to_s and char_s != t_to_s[char_t] : 
                return False
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s
        return True
