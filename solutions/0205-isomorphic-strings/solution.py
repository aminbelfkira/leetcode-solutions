# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/
# Accepted: 2026-09-18T13:07:23.000Z
# Language: Python3
# Runtime: 5 ms · Beats 51.73%
# Memory: 19.3 MB · Beats 48.2%
# Submission: https://leetcode.com/submissions/detail/2145751468/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        if len(s) != len(t) : 
            return False
        for s_char, t_char in zip(s,t) : 
            if s_char in s_to_t and s_to_t[s_char] != t_char : 
                return False
            if t_char in t_to_s and t_to_s[t_char] != s_char : 
                return False
            s_to_t[s_char] = t_char
            t_to_s[t_char] = s_char
        return True
