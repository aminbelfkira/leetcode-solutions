# 383. Ransom Note
# https://leetcode.com/problems/ransom-note/
# Accepted: 2026-07-20T22:48:45.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 13 ms · Beats 82.19%
# Memory: 19.7 MB · Beats 33.07%
# Submission: https://leetcode.com/submissions/detail/2075123102/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        from collections import Counter

        return Counter(ransomNote)<= Counter(magazine)
