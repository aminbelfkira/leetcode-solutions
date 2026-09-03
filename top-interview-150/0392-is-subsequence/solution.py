# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/
# Accepted: 2026-09-03T21:03:23.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 23 ms · Beats 2.84%
# Memory: 69.7 MB · Beats 7.6%
# Submission: https://leetcode.com/submissions/detail/2130097362/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if not s and not t : 
            return True
        elif not s : 
            return True
        elif not t : 
            return False
        elif s[0] != t[0] : 
            return self.isSubsequence(s, t[1:])
        else : 
            return self.isSubsequence(s[1:], t[1:])
