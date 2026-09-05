# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# Accepted: 2026-09-05T15:24:19.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 19 ms · Beats 19.74%
# Memory: 22.5 MB · Beats 41.29%
# Submission: https://leetcode.com/submissions/detail/2131860598/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagrams = defaultdict(list)

        for word in strs : 
            key = str(sorted(word)) 
            anagrams[key].append(word)
        return list(anagrams.values())
