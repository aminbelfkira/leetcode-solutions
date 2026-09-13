# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/
# Accepted: 2026-09-13T21:29:47.000Z
# Language: Python3
# Runtime: 19 ms · Beats 2.86%
# Memory: 69.9 MB · Beats 7.73%
# Submission: https://leetcode.com/submissions/detail/2141027619/

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
        return self.isSubsequence(s, t[1:])
