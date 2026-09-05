# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/
# Accepted: 2026-09-05T21:35:29.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 47 ms · Beats 47.83%
# Memory: 39.4 MB · Beats 21.95%
# Submission: https://leetcode.com/submissions/detail/2132172955/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices = {}

        for i,num in enumerate(nums) : 

            if num in indices and abs(i - indices[num])<= k :
                return True
            indices[num] = i
        return False
