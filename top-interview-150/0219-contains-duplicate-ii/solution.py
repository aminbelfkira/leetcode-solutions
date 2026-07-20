# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/
# Accepted: 2026-07-20T23:55:27.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 43 ms · Beats 19.24%
# Memory: 39.5 MB · Beats 5.69%
# Submission: https://leetcode.com/submissions/detail/2075141126/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        seen = {}

        for i, num in enumerate(nums) : 

            if num in seen : 
                if abs(seen[num] - i) <= k : 
                    return True
            seen[num] = i
        return False
