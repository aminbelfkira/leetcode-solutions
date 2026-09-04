# 383. Ransom Note
# https://leetcode.com/problems/ransom-note/
# Accepted: 2026-09-04T13:45:52.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 19 ms · Beats 63.85%
# Memory: 19.6 MB · Beats 73.05%
# Submission: https://leetcode.com/submissions/detail/2130751608/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter

        return Counter(ransomNote) <= Counter(magazine)
