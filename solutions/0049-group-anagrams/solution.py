# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# Accepted: 2026-09-14T20:33:56.000Z
# Language: Python3
# Runtime: 19 ms · Beats 19.69%
# Memory: 22.4 MB · Beats 41.3%
# Submission: https://leetcode.com/submissions/detail/2141989733/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagrams = defaultdict(list)

        for word in strs : 
            key = str(sorted(word))
            anagrams[key].append(word)
        
        return list(anagrams.values())
