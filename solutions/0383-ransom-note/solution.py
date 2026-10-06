# 383. Ransom Note
# https://leetcode.com/problems/ransom-note/
# Accepted: 2026-10-06T12:36:39.000Z
# Language: Python3
# Runtime: 16 ms · Beats 66.68%
# Memory: 19.7 MB · Beats 9.08%
# Submission: https://leetcode.com/submissions/detail/2164219005/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter

        return Counter(ransomNote) <= Counter(magazine)
