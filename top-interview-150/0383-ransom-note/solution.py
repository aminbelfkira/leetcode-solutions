# 383. Ransom Note
# https://leetcode.com/problems/ransom-note/
# Accepted: 2026-09-05T11:33:54.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 17 ms · Beats 65.67%
# Memory: 19.7 MB · Beats 34.22%
# Submission: https://leetcode.com/submissions/detail/2131654399/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter

        return Counter(ransomNote) <= Counter(magazine)
