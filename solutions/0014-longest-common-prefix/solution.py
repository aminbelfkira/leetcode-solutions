# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
# Accepted: 2026-09-11T21:02:16.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 31.96%
# Submission: https://leetcode.com/submissions/detail/2138969695/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = ""

        for prefixs in zip(*strs) : 
            if len(set(prefixs)) ==1 : 
                prefix += prefixs[0]
            else : 
                return prefix
        return prefix        
