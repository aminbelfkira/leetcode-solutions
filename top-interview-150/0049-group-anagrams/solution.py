# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# Accepted: 2026-07-20T23:26:43.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 11 ms · Beats 82.98%
# Memory: 22.1 MB · Beats 53.37%
# Submission: https://leetcode.com/submissions/detail/2075133288/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import defaultdict
        anagrams = defaultdict(list)

        for word in strs : 
            key = "".join(sorted(word))
            anagrams[key].append(word)

        return list(anagrams.values())
