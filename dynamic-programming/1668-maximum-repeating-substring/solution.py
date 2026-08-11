# 1668. Maximum Repeating Substring
# https://leetcode.com/problems/maximum-repeating-substring/
# Accepted: 2026-08-11T02:09:03.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 0 ms · Beats 100%
# Memory: 19.1 MB · Beats 86.22%
# Submission: https://leetcode.com/submissions/detail/2102173173/

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        
        k = 0 
        while word * k in sequence : 
            k+=1
        return k -1
