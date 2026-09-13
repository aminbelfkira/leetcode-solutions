# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/
# Accepted: 2026-09-13T21:31:24.000Z
# Language: Python3
# Runtime: 39 ms · Beats 88.02%
# Memory: 39.5 MB · Beats 12.35%
# Submission: https://leetcode.com/submissions/detail/2141028233/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, num in enumerate(nums) : 
            if num in seen and abs(seen[num]-i) <= k :
                return True
            seen[num] = i
        return False
