# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
# Accepted: 2026-09-03T20:39:21.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 4 ms · Beats 7.49%
# Memory: 19.4 MB · Beats 7.25%
# Submission: https://leetcode.com/submissions/detail/2130085848/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs : 
            return ""
        for i, chars in enumerate(zip(*strs)) :
            print(chars)
            if len(set(chars)) >1 : 
                return strs[0][:i]
        return min(strs, key=len)
                    

        
        
