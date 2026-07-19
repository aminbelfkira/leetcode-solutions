# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Accepted: 2026-07-19T01:34:29.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 3 ms · Beats 80.22%
# Memory: 20.5 MB · Beats 36.12%
# Submission: https://leetcode.com/submissions/detail/2072874006/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for idx, num in enumerate(numbers) : 

            if num in seen : 
                return sorted([idx +1, seen[num] +1])
            seen[target - num] = idx
        
        return 
