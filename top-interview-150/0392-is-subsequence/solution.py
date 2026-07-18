# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/
# Accepted: 2026-07-18T19:25:08.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 19 ms · Beats 2.91%
# Memory: 69.7 MB · Beats 6.93%
# Submission: https://leetcode.com/submissions/detail/2072743865/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if not s : 
            return True
        
        if not t : 
            return False
        
        if s[0] == t[0] : 
            return self.isSubsequence(s[1:], t[1:])
        
        return self.isSubsequence(s, t[1:])
