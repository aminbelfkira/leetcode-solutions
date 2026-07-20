# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/
# Accepted: 2026-07-20T21:49:46.000Z
# Language: Python3
# Runtime: 19 ms · Beats 2.85%
# Memory: 70 MB · Beats 6.9%
# Submission: https://leetcode.com/submissions/detail/2075105188/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if not s : 
            return True
        if not t :
            return False
        if s[0] != t[0] : 
            return self.isSubsequence(s, t[1:])
        return self.isSubsequence(s[1:], t[1:])
