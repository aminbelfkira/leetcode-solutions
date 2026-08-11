# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/
# Accepted: 2026-08-11T00:08:29.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 19 ms · Beats 2.8%
# Memory: 69.8 MB · Beats 6.87%
# Submission: https://leetcode.com/submissions/detail/2102123104/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s: 
            return True
        # Si t est vide mais pas s, alors s n'est pas une sous-suite
        if not t: 
            return False
        
        if s[0] == t[0]:
            # Match ! On avance dans les deux chaînes
            return self.isSubsequence(s[1:], t[1:])
        else:
            # Pas de match, on cherche le caractère s[0] plus loin dans t
            return self.isSubsequence(s, t[1:])
        
