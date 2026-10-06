# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
# Accepted: 2026-10-06T14:33:33.000Z
# Language: Python3
# Runtime: 0 ms · Beats 100%
# Memory: 19.4 MB · Beats 33.01%
# Submission: https://leetcode.com/submissions/detail/2164332387/

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        k = 0
        longest = ''
        for chars in zip(*strs) : 
            if len(set(chars)) ==1 : 
                k+=1
                longest += chars[0]
            else : 
                break
        return longest
