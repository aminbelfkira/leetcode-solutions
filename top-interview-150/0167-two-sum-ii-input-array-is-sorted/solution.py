# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Accepted: 2026-09-03T21:08:39.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 3 ms · Beats 79.59%
# Memory: 20.7 MB · Beats 8.5%
# Submission: https://leetcode.com/submissions/detail/2130099637/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        seen = {}

        for i, num in enumerate(numbers) : 

            if num in seen : 
                return [seen[num] +1 , i +1]
            seen[target - num] = i 
        print(seen)
        
