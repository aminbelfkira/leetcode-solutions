# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/
# Accepted: 2026-10-06T15:03:45.000Z
# Language: Python3
# Runtime: 22 ms · Beats 3.09%
# Memory: 69.7 MB · Beats 8.24%
# Submission: https://leetcode.com/submissions/detail/2164363135/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s and not t : 
            return True
        if not s and t :
            return True
        if s and not t :
            return False 
        if s[0] == t[0] : 
            return self.isSubsequence(s[1:], t[1:])
        else : 
            return self.isSubsequence(s, t[1:])
