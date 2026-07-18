# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
# Accepted: 2026-07-18T23:38:25.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 3 ms · Beats 20.43%
# Memory: 19.3 MB · Beats 72.81%
# Submission: https://leetcode.com/submissions/detail/2072844748/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs : 
            return ""
        
        for i, chars in enumerate(zip(*strs)) : 
            if len(set(chars)) >1 : 
                return strs[0][:i]
        
        return min(strs, key=len)
